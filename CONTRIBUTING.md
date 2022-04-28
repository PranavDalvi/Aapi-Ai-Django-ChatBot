# Contribution Guide 🤖
The project is built with Django and HTML, CSS, JS.

## Local Setup
- [Fork](https://github.com/PranavDalvi/Django-ChatBot/fork) this repository.
- *Note: You need python and some of its libries like (django, nltk, numpy, tensorflow) to run and test the code which can be install pip*
- requirements.txt has details of all the dependencies which are needed to run this project. To run the project steps are given below:

- To understand the steps given below you should know how to create new Django project and Python virtual environment.
1. Create a new Django project. (why? because we will be needing secret key to run the project)
2. Open the newly created Django project and copy the full string of secret key from `settings.py`.
3. Now open the ChatBot project then open the project folder and create the new file named as `.env` and paste the secret key.
- .env file should look like this:
```
SECRET_KEY = 'dlm*zt#1-3g!xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```
4. Now Download the requirements from requirements.txt (Python virtual environment is required).
5. Do the migrations and run the project.

## Hello First-time Contributors 👋
- There are lot of resources (articles, courses, videos) available for getting started with git and GitHub you can search and follow any of the resource you like.
- You can pick any of the issues from [Issues](https://github.com/PranavDalvi/Django-ChatBot/issues) or If you feel like it needs extra feature or if you find bug, you can create your own issue.
- You can drop a comment on issue saying "Hi, let me work on this" to avoid multiple people working on the same PR.
- Lastly, It is fine if you mess something up. If there is anything wrong in the PR I will let you know how to fix that in comments of the PR.
- If you are still scared to drop a PR or need any help, you can always drop us an email at groupchatbot01@gmail.com.
