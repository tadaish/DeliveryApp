from django.contrib import admin
from .models import Shipper, User, Client, Order

# Register your models here.
admin.site.register(Shipper)
admin.site.register(Client)
admin.site.register(Order)
