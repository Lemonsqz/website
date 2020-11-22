from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from base.models import *


class PhoneAdmin(SummernoteModelAdmin):
    summernote_fields = ('img', 'title', 'description', 'add_img',)


class AccessoryAdmin(SummernoteModelAdmin):
    summernote_fields = ('img', 'title', 'description', 'add_img',)


class NotebookAdmin(SummernoteModelAdmin):
    summernote_fields = ('img', 'title', 'description', 'add_img',)


admin.site.register(Phone, PhoneAdmin)
admin.site.register(Accessory, AccessoryAdmin)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)
admin.site.register(Category)

