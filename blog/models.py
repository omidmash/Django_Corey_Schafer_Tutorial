from django.db import models
from django.utils import timezone
#django has automatically created a User database.
from django.contrib.auth.models import User

'''
In models we create classes that are then created/represented(?) in the
database. 
These classes have to inherit from models.Model.
CharField is for limited text(?), TextField for unlimited, and
DateTimeField has default=timezone.now imported from django.utils
timezone.
ForeignKey is for one to many (one user many posts) and it takes User
that was imported. On_delete does something once the user doesn't exist.
'''


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE   )

    # dunder? __ __ : so we can use Post.objects to access data
    # in string form. Now it returns it's title.
    def __str__(self):
        return self.title
