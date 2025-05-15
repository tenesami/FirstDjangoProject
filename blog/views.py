from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})












# def home(request):
#     return HttpResponse("<h1>Welcome to the Blog Home Page</h1>")

# def about(request):
#     return HttpResponse("<h1>About the Blog</h1>")
