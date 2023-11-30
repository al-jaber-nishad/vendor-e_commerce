from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import serializers

# from authentication.models import User

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['id', 'email', 'first_name', 'last_name', 'username']

