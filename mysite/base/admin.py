from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from base.models import Product


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('img', 'title', 'description', 'add_img',)


admin.site.register(Product, ProductAdmin)
