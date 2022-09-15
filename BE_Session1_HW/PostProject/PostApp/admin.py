from django.contrib import admin
from .models import User, Comment, Category, Likes, Major1st, Major2nd, Post

# Register your models here.
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Likes)
admin.site.register(Major1st)
admin.site.register(Major2nd)
admin.site.register(Post)