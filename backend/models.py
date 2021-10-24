from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator

# Create your models here.
class User(AbstractUser):
    picture = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')
    contact = models.CharField(max_length=10, validators=[MinLengthValidator(10)], null=True, blank=False)
    contrib = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Category(models.Model):
    name = models.TextField()
    priority = models.IntegerField(default=0)

class Organisation(models.Model):
    name = models.TextField()
    registrant = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    video = models.FileField(upload_to='audio/')

    class Meta:
        db_table = 'Audio_store'

    def __str__(self):
        return self.name

class Campaign(models.Model):
    org = models.ForeignKey(Organisation, null=True, blank=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=False, on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=True)
    requirement = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    name = models.TextField()
    description = models.TextField()
    blog = models.TextField()

    def __str__(self):
        return self.name

class Ruby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)

class Queue(models.Model):
    name = models.CharField(max_length=2, default="p1")
    priority = models.IntegerField(default=0, blank=False, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    process = models.ForeignKey(Campaign, null=True, blank=False, on_delete=models.CASCADE)
    queue = models.ForeignKey(Queue, null=True, blank=False, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    quantum = models.IntegerField(default=4)

class State(models.Model):
    cur = models.ForeignKey(Item, null=True, blank=True, on_delete=models.CASCADE)
    funds = models.IntegerField(default=0)

class ContactUs(models.Model):
    From = models.TextField()
    subject = models.TextField()
    message = models.TextField()
    email = models.TextField()
