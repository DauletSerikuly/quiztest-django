from django.contrib import admin
from .models import Lecture
from tests.models import Test

admin.site.register(Lecture)
admin.site.register(Test)
