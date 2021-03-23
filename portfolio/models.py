from django.db import models


# Create your models here.
class About(models.Model):
    image = models.ImageField()
    profile_img = models.ImageField()
    title = models.CharField(max_length=150,blank=False)
    birthday = models.CharField(max_length=30)
    age = models.IntegerField()
    company = models.CharField(max_length=50)
    degree = models.CharField(max_length=150)
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    city = models.CharField(max_length=150)
    freelance = models.CharField(max_length=20)

class Facts(models.Model):
    happy_client = models.IntegerField()
    project = models.IntegerField()
    support_hour = models.IntegerField()
    worker = models.IntegerField()

class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    percent = models.IntegerField()

class Summary(models.Model):
    name = models.CharField(max_length=150)
    some_word = models.CharField(max_length=1000)
    bullet1 = models.CharField(max_length=500, null=True)
    bullet2 = models.CharField(max_length=500, null=True)
    bullet3 = models.CharField(max_length=500, null=True)
    
class Experience(models.Model):
    title = models.CharField(max_length=150)
    date = models.CharField(max_length=30)
    place = models.CharField(max_length=150)
    bullet1 = models.CharField(max_length=500, null=True)
    bullet2 = models.CharField(max_length=500, null=True)
    bullet3 = models.CharField(max_length=500, null=True)


class Education(models.Model):
    degree = models.CharField(max_length=150)
    date = models.CharField(max_length=150)
    institution = models.CharField(max_length=300)
    some_word = models.CharField(max_length=500)

class Portfolio(models.Model):
    image = models.ImageField()

class Service(models.Model):
    service = models.CharField(max_length=30)
    some_word = models.CharField(max_length=500)

class Testimonial(models.Model):
    other_word = models.CharField(max_length=200)
    image = models.ImageField()
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=50)

class Contact(models.Model):
    location = models.CharField(max_length=300)
    email = models.EmailField()
    call = models.CharField(max_length=14)
    google_map = models.TextField()

class Email_Contact(models.Model):
    name = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=50,null=False)
    subject = models.CharField(max_length=50,null=False)
    message = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.email
