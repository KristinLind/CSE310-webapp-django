from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_client, name='add_client'),
    path('client/<str:client_id>/', views.client_detail, name='client_detail'),
    path('client/<str:client_id>/update/', views.update_client, name='update_client'),
    path('client/<str:client_id>/delete/', views.delete_client, name='delete_client'),
]