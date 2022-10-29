from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    images = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name