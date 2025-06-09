from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView,

)
from .models import Post



# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5  # Number of posts per page

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5  # Number of posts per page

    def get_queryset(self): 
        # This method filters the posts to only include those authored by the user specified in the URL.
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # The 'username' is passed as a keyword argument in the URL.
        # The get_queryset method retrieves the posts authored by the specified user.
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    # template_name = 'blog/post_detail.html'  # <app>/<model>_<viewtype>.html
    # context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # This method sets the author of the post to the currently logged-in user before saving the form.
    # It ensures that the post is associated with the user who created it.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # This method sets the author of the post to the currently logged-in user before saving the form.
    # It ensures that the post is associated with the user who created it.

    # template_name = 'blog/post_form.html'  # <app>/<model>_<viewtype>.html
    # success_url = '/'

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
        return self.request.user == post.author   
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # redirects to home page after deletion
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})












# def home(request):
#     return HttpResponse("<h1>Welcome to the Blog Home Page</h1>")

# def about(request):
#     return HttpResponse("<h1>About the Blog</h1>")
