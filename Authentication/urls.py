from django.urls import path, include
from Authentication.views import login_user, register_user

app_name = 'Authentication'

urlpatterns = [
    path('', login_user, name = 'login-user'),
    path('register/', register_user, name = 'register-user')
]