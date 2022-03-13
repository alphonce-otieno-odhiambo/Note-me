from django.db import models

# Create your models here.
class Note(models.Model):
    body=models.TextField(max_length=500, null=True, blank=True),
    update = models.DateTimeField(auto_now=True),
    created = models.DateField(auto_now_add=True),


    def ___str__(self):
        return self.body