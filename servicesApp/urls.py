from django.urls import path
from .views import ServicesList, ServicesDetail

urlpatterns = [
    path('services/', ServicesList.as_view(), name='services_list'),
    path('services/<int:pk>/', ServicesDetail.as_view(), name='services_detail'),
]
