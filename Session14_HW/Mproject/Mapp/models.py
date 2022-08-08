from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 지정 책 1권의 게시판
POST_CHOICES = (
    ('일반', '일반'),
    ('서평', '서평'),
    ('공지', '공지'),
    ('투표', '투표'),
)

class BookPost(models.Model):
    category = models.CharField(max_length=20, choices=POST_CHOICES, blank=True)
    Book_title = models.CharField(max_length=50)
    Book_content = models.TextField()
    Book_author = models.ForeignKey(User, models.CASCADE, related_name="bookauthor")

    def __str__(self):
        return self.Book_title


class BookComment(models.Model):
    B_post = models.ForeignKey(BookPost, on_delete=models.CASCADE, related_name='bookcomments')
    B_content = models.TextField()
    B_author = models.ForeignKey(User, models.CASCADE, related_name="bcauthor")

    def __str__(self):
        return self.B_content


# 지정 영화 1편의 게시판
class MoviePost(models.Model):
    category = models.CharField(max_length=20, choices=POST_CHOICES, blank=True)
    Movie_title = models.CharField(max_length=50)
    Movie_content = models.TextField()
    Movie_author = models.ForeignKey(User, models.CASCADE, related_name="movieauthor")

    def __str__(self):
        return self.Movie_title

class MovieComment(models.Model):
    M_post = models.ForeignKey(MoviePost, on_delete=models.CASCADE, related_name='moviecomments')
    M_content = models.TextField()
    M_author = models.ForeignKey(User, models.CASCADE, related_name="mcauthor")

    def __str__(self):
        return self.M_content


# 지정 드라마 1편의 게시판
class DramaPost(models.Model):
    category = models.CharField(max_length=20, choices=POST_CHOICES, blank=True)
    Drama_title = models.CharField(max_length=50)
    Drama_content = models.TextField()
    Drama_author = models.ForeignKey(User, models.CASCADE, related_name="dramaauthor")

    def __str__(self):
        return self.Drama_title

class DramaComment(models.Model):
    D_post = models.ForeignKey(DramaPost, on_delete=models.CASCADE, related_name='dramacomments')
    D_content = models.TextField()
    D_author = models.ForeignKey(User, models.CASCADE, related_name="dcauthor")

    def __str__(self):
        return self.D_content