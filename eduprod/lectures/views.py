from django.shortcuts import render, get_object_or_404
from .models import Lecture

def lecture_list(request):
    lectures = Lecture.objects.all()
    return render(request, 'lecture_list.html', {'lectures': lectures})

def lecture_detail(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    return render(request, 'lecture_detail.html', {'lecture': lecture})
