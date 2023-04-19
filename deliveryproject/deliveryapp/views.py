from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.views import Response

from .models import User, Client, Shipper, Order
from .serializer import UserSerializer, ClientSerializer, ShipperSerializer
from rest_framework.decorators import action


# Create your views here.
class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['current_user']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get', 'put'], detail=False, url_path='current-user')
    def current_user(self, request):
        u = request.user
        if request.method.__eq__('PUT'):
            for k, v in request.data.items():
                setattr(u, k, v)
            u.save()

        return Response(UserSerializer(u, context={'request': request}).data)


class ClientViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ShipperViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer
