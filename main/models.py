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
    
class Expert(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    village = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Market(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    village = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    crop = models.TextField()
    crop_qty = models.TextField()
    sell_time = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Donate(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    amount = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Partiner(models.Model):
    name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
