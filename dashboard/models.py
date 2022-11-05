from django.db import models
from ckeditor.fields import RichTextField


class Job(models.Model):
    title = models.CharField(max_length=200)
    responsibilities = RichTextField(blank=False)
    skills = RichTextField(blank=False)
    qualifications = RichTextField(blank=False)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def active(self):
        return self.status == 'Active'
        
    def expired(self):
        return self.status == 'Expired'

class Project(models.Model):
    name = models.CharField(max_length=200)    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class MultipleImage(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    images = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    