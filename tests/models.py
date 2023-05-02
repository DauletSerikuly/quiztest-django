from django.db import models
from lectures.models import Lecture

class Test(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions', default=1)
    text = models.TextField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.text