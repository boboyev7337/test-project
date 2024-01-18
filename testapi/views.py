from django.shortcuts import render

from testapi.models import Test


def index(request):
    # tests = Test.objects.all()
    # context = {
    #     'tests': tests
    # }
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def support(request):
    return render(request, 'support.html')