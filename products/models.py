from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

# My Custom Managers


class ActiveCommentManager(models.Manager):
    """
    This manager will return the active comments
    """
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(active=True)


# My Models


class Product(models.Model):
    title = models.CharField(_('title'), max_length=100)
    description = RichTextField(_('description'))
    short_description = models.TextField(_('short description'), blank=True)
    price = models.PositiveIntegerField(_('price'), default='0')
    quantity = models.PositiveIntegerField(_('quantity'), blank=True, null=True)
    active = models.BooleanField(default=True)
    cover = models.ImageField(_('image'), upload_to='covers/', default='covers/default_cover.jpg')

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def is_in_stock(self):
        return self.quantity > 0

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class Comment(models.Model):

    PRODUCT_STARS = (
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Very Good')),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name=_('comment text'))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('your score'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    # Managers
    objects = models.Manager()
    active_comments_manager = ActiveCommentManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
