# Generated by Django 4.1.1 on 2022-10-10 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_short_description_alter_product_cover_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default='0', verbose_name='price'),
        ),
    ]