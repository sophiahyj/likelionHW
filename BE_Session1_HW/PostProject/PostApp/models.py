from django.db import models

# Create your models here.
# 1. 게시판, 댓글 CRUD (o)
# 2. 카테고리 - 이름, 코드 -> 게시글과 연결 (o)
# 3. User: 사용자의 이름, 아이디, 비밀번호, 전공
# 4. 전공은 본전공 + 복수/융합/심화 전공 포함
# 5. 로그인한 사용자는 좋아요 표시 가능, 좋아요 누른 사용자수 표시해야 함

class Major1st(models.Model):
    Major1 = models.CharField(max_length=20)

    def __str__(self):
        return self.Major1

class Major2nd(models.Model):
    Major2 = models.CharField(max_length=20)

    def __str__(self):
        return self.Major2


class User(models.Model):
    name = models.CharField(max_length=20)
    user_id = models.CharField(max_length=20, blank=False)
    user_password = models.CharField(max_length=20, blank=False)
    major_1st = models.ManyToManyField(Major1st, related_name="major1")
    major_2nd = models.ManyToManyField(Major2nd, related_name='major2')

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    category_code = models.IntegerField()


class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete= models.CASCADE)
    post_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return self.content


class Likes(models.Model):
    like_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    like_user = models.ManyToManyField(User, related_name='likes')
    like_count = models.IntegerField()