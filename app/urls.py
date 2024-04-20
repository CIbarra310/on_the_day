from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('new_run', views.new_run, name="new_run"),
]
