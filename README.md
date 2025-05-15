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