from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=50, null=True, verbose_name='fullname')
    avatar = models.ImageField(upload_to='users/%Y/%m', null=True)
    is_shipper = models.BooleanField(default=False, verbose_name='shipper')
    is_client = models.BooleanField(default=False, verbose_name='client')

    def __str__(self):
        return self.username


class Shipper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id = models.CharField(max_length=12)
    phone = models.CharField(max_length=10)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.full_name


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.user.full_name


class Order(models.Model):
    STATUS_OF_ORDER = [
        (0, 'Huỷ '),
        (1, 'Hoàn Thành'),
        (2, 'Đang Giao')
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    from_address = models.CharField(max_length=200, null=True, verbose_name='from', )
    to_address = models.CharField(max_length=200, null=True, verbose_name='to')
    description = models.CharField(max_length=200)
    order_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='value')
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=STATUS_OF_ORDER)

    def __str__(self):
        return self.user.full_name
