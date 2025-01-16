from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('welcome/', views.welcome, name='welcome'),
    path('reserve/', views.reserve_meeting, name='reserve_meeting'),
    path('logout/', views.logout, name='logout'),
    path('delete/<int:meeting_id>/', views.delete_meeting, name='delete_meeting'),
]