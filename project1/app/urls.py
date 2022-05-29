from django.urls import path
from . import views

urlpatterns = [
    path('sample/', views.input),
    path('sample/output', views.output),
]
