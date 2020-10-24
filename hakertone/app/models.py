from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
class User_info(models.Model):
   user_id = models.IntegerField() 
   nickname = models.CharField(max_length=100)
   apartment = models.CharField(max_length=100)
   address = models.CharField(max_length=100)
   phone = models.IntegerField()

class Company(models.Model):
    user_id = models.IntegerField() 
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    img = models.ImageField(upload_to='images/', null=True)
    contents = models.TextField()

class Group_buying(models.Model):
    title = models.TextField()
    img = models.ImageField(upload_to='images/', null=True)
    proceeding = models.IntegerField()
    contents = RichTextUploadingField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    writer = models.IntegerField()
    category = models.IntegerField()
    apartment = models.CharField(max_length=100)

class Group_buying_comment(models.Model):
    Group_buying_id = models.IntegerField()
    user_info_id =  models.IntegerField()
    contents = models.TextField(null = True)
    date = models.DateTimeField(auto_now_add=True)
    
class Flee_market(models.Model):
    title = models.TextField()
    img = models.ImageField(upload_to='images/', null=True)
    img1 = models.ImageField(upload_to='images/', null=True)
    img2 = models.ImageField(upload_to='images/', null=True)
    contents = models.TextField(null = True)
    proceeding = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    writer = models.IntegerField()
    category = models.IntegerField()
    apartment = models.CharField(max_length=100)

class Company_buying(models.Model):
    company_id = models.IntegerField()
    contract = models.IntegerField()
    title = models.CharField(max_length=200)
    main_img = models.ImageField(upload_to='images/')
    detail_img1 = models.ImageField(upload_to='images/', null=True)
    detail_img2 = models.ImageField(upload_to='images/', null=True)
    contents = models.TextField()
    category = models.IntegerField()
    apartment = models.CharField(max_length=100)
    finish_date = models.DateField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    company_id = models.IntegerField()
    writer = models.IntegerField()
    grade = models.FloatField()
    contents = models.TextField()



