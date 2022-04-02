from cgitb import text
from dataclasses import field
from pydoc_data.topics import topics
from tabnanny import verbose
from django.db import models

class Response(models.Model):
    text = models.TextField()
    class meta:
        verbose_name_plural = "Responses"

    def __str__(self):
        return self.text


