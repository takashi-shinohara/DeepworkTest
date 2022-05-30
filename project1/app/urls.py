from django.urls import path
from . import views
from . import responseAI

urlpatterns = [
    path('sample/', views.input),
    path('sample/output', views.output),
    path('example.com/', responseAI.dummyAI),
]
