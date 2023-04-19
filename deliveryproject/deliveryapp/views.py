from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from .models import User, Client, Shipper, Order
from .serializer import UserSerializer, ClientSerializer, ShipperSerializer


# Create your views here.
class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClientViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ShipperViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer
