# Contribution Guide 🤖
The project is built with Django and HTML, CSS, JS.

## Local Setup
- [Fork](https://github.com/PranavDalvi/Django-ChatBot/fork) this repository.
- *Note: You need python and some of its libries like (django, nltk, numpy, tensorflow) to run and test the code which can be install using pipenv or pip*
- pipenv has details of all the dependencies which are needed to run this project just install pipenv and run sync. Steps are given below:

1. First clone the project
2. Create new folder where you want and copy `pipfile`, `pipfile.lock` and `jsonfile` from the cloned repo to the newly created folder.
- This is how your newly created project directory will look like
```
your_newly_created_folder/
    jsonfile
    pipfile
    pipfile.lock   
```
3. Now, open the terminal in the current working directory and run `pip install pipenv` then `pipenv sync` which will download dependencies.
4. Now, run `pipenv shell`, `django-admin startproject project .` which will create important files likes settings.py and manage.py and run `python manage.py startapp chatbot_project` which is our ChatBot's brain.
- This is how your newly created project directory will look like
```
your_newly_created_folder/
    project/
         __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
        
    chatbot_project/
        __init__.py
        admin.py
        apps.py
        migrations/
        __init__.py
        models.py
        tests.py
        views.py
        
    jsonfile
    pipfile
    pipfile.lock
```
5. Open the settings.py from your newly created project and add `'chatbot_project'` under INSTALLED_APPS.
- It should look like this:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'chatbot_project'
 ]
   ``` 
6. Now, go to the folder where you have cloned the Django-chatbot project from GitHub and open project folder from ther copy the `url.py` file and paste it into the newly created `project` folder
7. Now your done with `project` folder close it and open `chatbot_project` folder and copy the its contents from cloned repo to your newly created `django project's chatbot_project folder`
8. Hooray! we are done with copying stuff 🤩 now lets open terminal in your newly created project and run `python manage.py migrate`
9. And run `python manage.py runserver`

## Hello First-time Contributors 👋
- There are lot of resources (articles, courses, videos) available for getting started with git and GitHub you can search and follow any of the resource you like.
- You can pick any of the issues from [Issues](https://github.com/PranavDalvi/Django-ChatBot/issues) or If you feel like it needs extra feature or if you find bug, you can create your own issue.
- You can drop a comment on issue saying "Hi, let me work on this" to avoid multiple people working on the same PR.
- Lastly, It is fine if you mess something up. If there is anything wrong in the PR I will let you know how to fix that in comments of the PR.
- If you are still scared to drop a PR or need any help, you can always drop us an email at groupchatbot01@gmail.com.
