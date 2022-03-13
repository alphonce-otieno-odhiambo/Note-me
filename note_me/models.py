from django.db import models

# Create your models here.
class Note(models.Modal):
    body=models.TextField(max_length=500, null=True, blank=True),
    update = models.DateTimeField(auto_now=True),
    created = models.DateField(auto_now_add=True),

    def __setattr__(self):
        return self.body[0:50]