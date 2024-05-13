from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('new_run', views.new_run, name="new_run"),
    path('run_queue', views.run_queue, name="run_queue"),
    path('run_history', views.run_history, name="run_history"),
    path('run/<int:run_request_id>/', views.view_run, name='view_run'),
]
