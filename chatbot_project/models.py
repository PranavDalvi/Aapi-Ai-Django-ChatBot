from cgitb import text
from dataclasses import field
from pydoc_data.topics import topics
from tabnanny import verbose
from django.db import models

# class Topic(models.Model):
#     text = models.CharField(max_length=200)
#     def __str__(self):
#         return self.text

class Response(models.Model):
    # topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    class meta:
        verbose_name_plural = "Responses"

    def __str__(self):
        return self.text


