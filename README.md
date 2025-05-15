cd ~/Desktop/Django
brew install pipenv # brew install python@3.9
pipenv --python 3.9
pipenv install django  
code . 
open and look the pipfile -> to double chack the requriments 
pipenv shell  -> activate the venv similar to source 
django-admin startproject django_project -> create django_project .
delete django_project -> avoide duplicate 
django-admin startproject django_project  . -> tell django to use as project directory

python3 manage.py runserver

python manage.py startapp blog #-> to create new project 

To make a blog page to be home page for the entire website 
in the project urls leave the path to be " " empty the it will match the empty path 
in the projcet Urls and also empty path in the blog urls and return blog home page 

to config your page in the settng blog page blog.app


Admin page 
python manage.py makemigrations -> detect changes and ubdate db
python manage.py migrate -> run the changes 
python manage.py createsuperuser 

Creating Model 
python3 manage.py makemigrations -> use the route to check the update before u migrate
python manage.py sqlmigrate blog 0001 -> to see the change made in sql form
python3 manage.py migrate -> apply all migration 

Once the change is add to the data base we can query the database using these models by
running Django Python shell which will allow us to work with models interactively line by line 
python3 manage.py shell then import 
from blog.models import Post
from django.contrib.auth.models import User
User.objects.all()
User.objects.first()
User.objects.last()
User.objects.filter(username='TesfaMi')
User.objects.filter(username='TesfaMi').first()

To compture this in user variable to access the atribures of user
user = User.objects.filter(username='TesfaMi').first()
user.id --> return 1 // or user.username --> return tesfaMi

to see posts 
Post.objects.all()

To create post 
post_1 = Post(title='Blog 1', content='Firts Post Content', author=user)
Post.objects.all() -> still empty until we save the post 
post_1.save() 
Post.objects.all() -> show us what we created -> <QuerySet [<Post: Post object (1)>]>

to tell what we want to see when we print 
go to the model and add __str__() method then exit() the terminal and come back
Post.objects.all() -> <QuerySet [<Post: Blog 1>]>

post_2 = Post(title='Blog 2', content='Second Post Content', author_id=user.id)
post_2.save()
>>> Post.objects.all()
<QuerySet [<Post: Blog 1>, <Post: Blog 2>]>

post = Post.objects.first()
>>> post.content
'Firts Post Content'
post.date_posted
datetime.datetime(2025, 5, 15, 16, 24, 57, 759016, tzinfo=datetime.timezone.utc)
post.author -> User: TesfaMi
post.author.email -> tesfayeatomsa@gmail.com

user.post_set.all() -> tell as the user all posts
we can also create post using user.post.set 
user.post_set.create(title='Blog 3', content='Third Post Content!') i.e., no aurhor b/c 
Django knows that and no need to save Django save that too

insted of using dummy data at the view model to use actual data created at model diretory 
from .models import Post
and in the home function update 'posts': Post.objects.all() 

then run python3 manage.py runserver -> it pulls from your database

to format the date in to the way we like Visit the [Django Documentation](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#date) for more information fromat by editing

blog -> templet -> home i.e., edit post.date_posted|date:"F d, Y" 