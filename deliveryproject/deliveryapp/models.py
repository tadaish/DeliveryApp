from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/%Y/%m', null=True)

    def __str__(self):
        return self.username


class Shipper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fullname = models.CharField(max_length=50)
    id = models.CharField(max_length=12)
    birthday = models.DateField()

    def __str__(self):
        return self.fullname


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fullname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname


class Order(models.Model):
    STATUS_OF_ORDER = [
        (0, 'Huỷ '),
        (1, 'Hoàn Thành'),
        (2, 'Đang Giao')
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_OF_ORDER)
    active = models.BooleanField(default=True)
