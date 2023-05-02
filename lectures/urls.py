from django.urls import path
from .views import lecture_list, lecture_detail

urlpatterns = [
    path('', lecture_list, name='lecture_list'),
    path('lectures/<int:pk>/', lecture_detail, name='lecture_detail')
]