from django.db import models

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    file = models.FileField(upload_to='uploads/lectures/')
