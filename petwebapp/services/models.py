from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    category_name = models.CharField(max_length=255, verbose_name="Category:")

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = "Category:"
        verbose_name_plural = "Category:"
        
class UserService(models.Model):
    dt = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255, verbose_name="Email")
    phone = models.CharField(max_length=255, verbose_name="Phone")
    title = models.CharField(max_length=255, verbose_name="Service title")
    text = RichTextField(blank=True, null=True)
    # text = models.TextField()
    image = models.ImageField(upload_to="", null=True, blank=True, default=None, verbose_name="Image")
    title_tag = models.CharField(max_length=255, verbose_name="Title tag:", default="Other")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Category:", default="Other")
    likes = models.ManyToManyField(User, related_name="services_posts")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
    
    class Meta:
        verbose_name = "User Service"
        verbose_name_plural = "User Services"
