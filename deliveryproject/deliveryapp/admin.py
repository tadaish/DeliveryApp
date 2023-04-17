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
        return obj.user.fullname

    def email(self, obj):
        return obj.user.email


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'fullname', 'email', 'is_superuser', 'is_client', 'is_shipper',
                  'user_permissions', 'last_login', 'date_joined']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'fullname', 'email', 'date_joined', 'is_superuser', 'is_client',
                    'is_shipper']
    search_fields = ['username', 'first_name', 'last_name']
    list_filter = ['date_joined', 'is_superuser', 'is_client', 'is_shipper']

    form = UserForm


class ClientAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'phone', 'address']
    search_fields = ['fullname']

    def fullname(self, obj):
        return obj.user.fullname

    def email(self, obj):
        return obj.user.email


class OrderForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Order
        fields = '__all__'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'client', 'from_address', 'to_address', 'order_value', 'created_date', 'status']
    search_fields = ['pk', 'client']
    list_filter = ['created_date', 'status']
    form = OrderForm

    def client(self, obj):
        return self.user.fullname


admin.site.register(User, UserAdmin)
admin.site.register(Shipper, ShipperAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
