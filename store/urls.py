import uuid
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create_store/', views.create_store, name='create_store'),
    path('<uuid:store_id>/', views.view_store, name='view_store'),
]