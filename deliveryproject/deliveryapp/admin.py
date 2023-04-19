from django.contrib import admin
from .models import Shipper, User, Client, Order
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.

class ShipperForm(forms.ModelForm):
    class Meta:
        model = Shipper
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'full_name', 'email', 'is_superuser', 'is_shipper', 'is_client',
                  'user_permissions', 'last_login', 'date_joined', 'avatar']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class OrderForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Order
        fields = '__all__'


class ShipperAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'id', 'phone', 'email', 'birthday']
    search_fields = ['full_name']
    form = ShipperForm

    def full_name(self, obj):
        return obj.user.fullname

    def email(self, obj):
        return obj.user.email


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'email', 'date_joined', 'is_superuser', 'is_client', 'is_shipper']
    search_fields = ['username', 'full_name']
    list_filter = ['date_joined', 'is_superuser', 'is_client', 'is_shipper']

    form = UserForm


class ClientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'address']
    search_fields = ['full_name']

    form = ClientForm

    def full_name(self, obj):
        return obj.user.full_name

    def email(self, obj):
        return obj.user.email


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'client', 'from_address', 'to_address', 'order_value', 'created_date', 'status']
    search_fields = ['pk', 'client']
    list_filter = ['created_date', 'status']
    form = OrderForm

    def client(self, obj):
        return self.user.full_name


admin.site.register(User, UserAdmin)
admin.site.register(Shipper, ShipperAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
