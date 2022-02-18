from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from datetime import datetime, date


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

#class Profile(models.Model):
 #   user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  #  bio = models.TextField()
    
  #  def __str__(self):
  #      return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', null=True, blank=True, )
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)  
    category = models.CharField(max_length=250, default='coding')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_post', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' |' + str(self.author)

    def number_of_likes(self):
        return self.likes.count()
    
    def get_absolute_url(self):
        return reverse('home')
   

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
