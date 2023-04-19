from django.urls import path, include
from rest_framework import routers
from . import views

r = routers.DefaultRouter()
r.register('users', views.UserViewSet, basename='user')
r.register('clients', views.ClientViewSet, basename='client')
r.register('shipper', views.ShipperViewSet, basename='shipper')

urlpatterns = [
    path('', include(r.urls)),
]
