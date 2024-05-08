from django.shortcuts import render
from .models import Blog


# Create your views here.
def home(request):

    queryset = Blog.objects.all()

    context = {
        'queryset': queryset
    }
    return render(request, 'home.html', context)