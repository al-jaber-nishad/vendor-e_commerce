from authentication.views import user_view as views
from django.urls import path

urlpatterns = [
	
	path('user_list', views.get_user_list),

]