from django.contrib import admin
from django.urls import path, include
from lectures.views import lecture_list

app_name = 'lectures'
app_name = 'tests'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lectures.urls')),
    path('tests/', include('tests.urls')),
]

