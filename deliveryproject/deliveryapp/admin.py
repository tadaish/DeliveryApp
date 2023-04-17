from django.contrib import admin
from .models import Shipper, User, Client, Order
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.

class ShipperForm(forms.ModelForm):
    class Meta:
        model = Shipper
        fields = '__all__'


class ShipperAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'id', 'phone', 'email', 'birthday']
    search_fields = ['fullname']
    form = ShipperForm

    def fullname(self, obj):
        return obj.user.get_full_name()

    def email(self, obj):
        return obj.user.email


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'is_superuser', 'is_client',
                    'is_shipper']
    search_fields = ['username', 'first_name', 'last_name']
    list_filter = ['date_joined', 'is_superuser', 'is_client', 'is_shipper']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'phone', 'address']
    search_fields = ['fullname']

    def fullname(obj):
        return obj.user.get_full_name()
    
    def email(self, obj):
        return obj.user.email


admin.site.register(User, UserAdmin)
admin.site.register(Shipper, ShipperAdmin)
admin.site.register(Client, ClientAdmin)
