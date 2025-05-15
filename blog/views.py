from django.shortcuts import render


posts = [
    {
    'author': 'John Doe',
    'title': 'Blog Post 1',
    'content': 'This is the content of the first blog post.',
    'date_posted': 'August 27, 2023'
    },
{
    'author': 'Jane Smith',
    'title': 'Blog Post 2',
    'content': 'This is the content of the second blog post.',
    'date_posted': 'August 28, 2023'
},
{
    'author': 'Alice Johnson',
    'title': 'Blog Post 3',
    'content': 'This is the content of the third blog post.',
    'date_posted': 'August 29, 2023'
}]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})












# def home(request):
#     return HttpResponse("<h1>Welcome to the Blog Home Page</h1>")

# def about(request):
#     return HttpResponse("<h1>About the Blog</h1>")
