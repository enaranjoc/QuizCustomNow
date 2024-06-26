from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import signup_view, login_view, home_view

urlpatterns = [
    path('home/', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
