from authentication.views import user_view as views
from django.urls import path

urlpatterns = [
	
	path('api/v1/user/get_user_list/', views.get_user_list),

]