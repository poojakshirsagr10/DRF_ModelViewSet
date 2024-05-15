from django.urls import path
from . import views

urlpatterns=[
    path('create/', views.create_api),
    path('show/', views.show_api),
    path('show/<pk>/', views.retrive_api),
    path('update/<pk>/', views.update_api),
    path('delete/<pk>/', views.delete_api)
]