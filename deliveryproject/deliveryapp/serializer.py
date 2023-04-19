from rest_framework import serializers
from .models import User, Client, Shipper, Order


class UserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='avatar')

    def get_image(self, user):
        if user.avatar:
            request = self.context.get('request')
            return request.build_absolute_uri('/static/%s' % user.avatar.name) if request else ''

    def create_user(self, validated_data):
        data = validated_data.copy()
        u = User(**data)
        u.set_password(u.password)
        u.save()
        return u

    class Meta:
        model = User
        fields = ['pk', 'username', 'password', 'full_name', 'email', 'is_superuser', 'is_shipper', 'is_client',
                  'avatar', 'image']
        extra_kwargs = {
            'avatar': {'write_only': True},
            'password': {'write_only': True}
        }


class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = ['full_name', 'id', 'phone', 'email', 'birthday']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['full_name', 'email', 'phone', 'address']
