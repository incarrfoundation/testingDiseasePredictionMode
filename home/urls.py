from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_view, name='upload'),
    path('result/<int:diagnosis_id>/', views.result_view, name='result'),
]
