from accounts.views import UserAdd, MyProfile, SuccessfulLogin, NeedRegistration
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('registration', UserAdd.as_view(), name='registration'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('my_profile', MyProfile.as_view(), name='my_profile'),
    path('successful_login', SuccessfulLogin.as_view(), name='success'),
    path('need_registration', NeedRegistration.as_view(), name='need_registration')
]

