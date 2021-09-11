from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
