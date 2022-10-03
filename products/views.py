from django.views import generic
from django.shortcuts import get_object_or_404, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _

from .models import Product, Comment
from .forms import CommentForm


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(SuccessMessageMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    success_message = _('Your comment created successfully')
    # def get_success_url(self):
    #     return reverse('products_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = self.kwargs['product_id']
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        return super().form_valid(form)
