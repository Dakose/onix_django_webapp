from django.db import models
from django.contrib.auth.models import User
  

class UserService(models.Model):
    dt = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255, verbose_name="Email:")
    phone = models.CharField(max_length=255, verbose_name="Phone:")
    title = models.CharField(max_length=255, verbose_name="Service title:")
    text = models.TextField()
    image = models.ImageField(upload_to="serviceimg/")
    title_tag = models.CharField(max_length=255, verbose_name="Title tag:")

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    class Meta:
        verbose_name = "User Service"
        verbose_name_plural = "User Services"
