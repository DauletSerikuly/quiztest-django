from django.urls import path
from .views import test_list, test_detail

urlpatterns = [
    path('tests/', test_list, name='test_list'),
    path('tests/<int:pk>/', test_detail, name='test_detail'),
]
