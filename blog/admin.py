from django.contrib import admin
# import the recently created Post class here
from .models import Post

# Register your models here.
admin.site.register(Post)
