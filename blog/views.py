from django.shortcuts import render

# Create your views here.

def post_list(request):
    """ Render a list of all posts.
    """
    return render(request, 'blog/post_list.html', {})
