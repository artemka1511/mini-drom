from accounts.views import UserAdd, MyProfile
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('registration', UserAdd.as_view(), name='registration'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('my_profile', MyProfile.as_view(), name='my_profile')
]

