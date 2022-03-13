
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='getroutes'),
    path('notes/', views.getNotes, name='getNotes'),
    path('note/<str:pk>/', views.getNotes, name='note'),
]
