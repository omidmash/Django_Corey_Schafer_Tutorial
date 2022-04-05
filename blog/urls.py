from django.urls import path
from . import views
'''Main URL routes here, minus the part given.
path is auto imported, and from root we import the views file,
which we then reference. path syntax: URL, where to, name'''

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
