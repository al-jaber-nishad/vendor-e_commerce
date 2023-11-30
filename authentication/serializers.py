from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import serializers

from authentication.models import Profile

# from authentication.models import User

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
     image = serializers.SerializerMethodField()
     role = serializers.SerializerMethodField()
     two_step_verified = serializers.SerializerMethodField()
     class Meta:
          model = User
          fields = ['id', 'email', 'first_name', 'last_name', 'username', 'image', 'role', 'two_step_verified', 'last_login', 'date_joined']


     def get_image(self, obj):
          instance = Profile.objects.get(user=obj)
          return instance.image

     def get_role(self, obj):
          instance = Profile.objects.get(user=obj)
          return instance.role

     def get_two_step_verified(self, obj):
          instance = Profile.objects.get(user=obj)
          return instance.two_step_verified