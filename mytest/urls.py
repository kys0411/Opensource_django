from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('test/<int:id>/', views.test),
    path('result/<int:id>/', views.result),
    path('stats/', views.stats)
]
