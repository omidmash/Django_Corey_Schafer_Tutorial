from django.contrib import admin
from .models import Post
'''
make it visible in admin GUI. 
Import from .models Post.
admin.site.register(variable)

'''

# Register your models here.
admin.site.register(Post)
