from django.contrib import admin
from .models import BookPost, BookComment, MoviePost, MovieComment, DramaPost, DramaComment

# Register your models here.
admin.site.register(BookPost)
admin.site.register(BookComment)
admin.site.register(MoviePost)
admin.site.register(MovieComment)
admin.site.register(DramaPost)
admin.site.register(DramaComment)