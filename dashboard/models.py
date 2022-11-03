from django.db import models
from ckeditor.fields import RichTextField

class Job(models.Model):
    title = models.CharField(max_length=200)
    responsibilities = RichTextField(blank=False)
    skills = RichTextField(blank=False)
    qualifications = RichTextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    