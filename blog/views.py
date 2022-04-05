from django.shortcuts import render
from .models import Post

'''
HTTPResponse for short stuff directly here, whilst render allows us to work with
templates. Should be auto  imported. 
We then created a list of dictionaries named posts.

Now we import .models import Post class, and use that instead.
'''

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2022',
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2022',
#     }
# ]

'''
in these functions the input of requests is needed by django. context is then equal to a dictionary,
where the key is posts and it references to the posts list we made earlier.
home then renders from templates/blog/home.html, and processes context.
about does the same but without context, and instead of that, we added title in a dictionary.
Syntax for render is request(django mandatory), where from, what should go in (title?)
'''


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

