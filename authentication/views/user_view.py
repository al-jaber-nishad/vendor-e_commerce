from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from authentication.serializers import UserListSerializer


@api_view(['GET'])
def get_user_list(request):
    users = User.objects.all()
    total_elements = users.count()

    page = request.query_params.get('page')
    size = request.query_params.get('size')

    serializer = UserListSerializer(users, many=True)

    response = {
        'users': serializer.data,
        'total_elements': total_elements,
    }

    return render(request, 'user/user_list.html', {'response': response})
