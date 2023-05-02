from django.shortcuts import render, get_object_or_404
from .models import Test

def test_list(request):
    tests = Test.objects.all()
    return render(request, 'test_list.html', {'tests': tests})

def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    return render(request, 'test_detail.html', {'test': test})

# Create your views here.
