from django.db import models

class User_info(models.Model):
   user_id = models.IntegerField() 
   nickname = models.CharField(max_length=100)
   apartment = models.CharField(max_length=100)
   address = models.CharField(max_length=100)

class Company(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    img = models.ImageField(upload_to='images/')
    contents = models.TextField()

class Group_buying(models.Model):
    title = models.TextField()
    img = models.ImageField(upload_to='images/')
    proceeding = models.IntegerField()
    contents = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    writer = models.IntegerField()
    category = models.IntegerField()

class Group_buying_comment(models.Model):
    Group_buying_id = models.IntegerField()
    user_info_id =  models.IntegerField()
    contents = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
class Flee_market(models.Model):
    title = models.TextField()
    img = models.ImageField(upload_to='images/')
    img1 = models.ImageField(upload_to='images/')
    img2 = models.ImageField(upload_to='images/')
    contents = models.TextField()
    proceeding = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    writer = models.IntegerField()
    category = models.IntegerField()

class Company_buying(models.Model):
    company_id = models.IntegerField()
    contract = models.IntegerField()
    main_img = models.ImageField(upload_to='images/')
    detail_img1 = models.ImageField(upload_to='images/')
    detail_img2 = models.ImageField(upload_to='images/')
    remark = models.IntegerField()
    contents = models.TextField()
    title = models.TextField()

class Review(models.Model):
    company_id = models.IntegerField()
    writer = models.IntegerField()
    grade = models.FloatField()
    contents = models.TextField()



