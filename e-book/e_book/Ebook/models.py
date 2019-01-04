from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    author_name = models.CharField(max_length=500)
    no_of_pages = models.IntegerField()
    tags = models.CharField(max_length=500)
    public = models.BooleanField(default=True)
    filename = models.CharField(max_length=500)

class User(models.Model):
    name = models.CharField(max_length=500)
    user_id = models.CharField(max_length=500, primary_key=True)
    password = models.CharField(max_length=500)
    storage_size = models.IntegerField(default=2048)

class User_Book(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
