from django.db import models

class StatusService(models.Model):
    StatusName = models.CharField(max_length=255, verbose_name="Status name:")

    def __str__(self):
        return self.StatusName 

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"    

class UserService(models.Model):
    service_dt = models.DateTimeField(auto_now=True)
    user_fname = models.CharField(max_length=255, verbose_name="First Name:")
    user_lname = models.CharField(max_length=255, verbose_name="Last Name:")
    user_email = models.CharField(max_length=255, verbose_name="Email:")
    user_phone = models.CharField(max_length=255, verbose_name="Phone:")
    services_name = models.CharField(max_length=255, verbose_name="Service name:")
    services_text = models.CharField(max_length=255, verbose_name="About services:")
    services_image = models.ImageField(upload_to="serviceimg/")
    services_status = models.ForeignKey(StatusService, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Status:")

    def __str__(self):
        return self.services_name
    
    class Meta:
        verbose_name = "User Service"
        verbose_name_plural = "User Services"

class UserComment(models.Model):
    comment_dt = models.DateTimeField(auto_now=True)
    comment_name = models.CharField(max_length=255, verbose_name="Comment name:")
    comment_text = models.CharField(max_length=255, verbose_name="Comment text:")

    def __str__(self):
        return self.comment_name

    class Meta:
        verbose_name = "User comment"
        verbose_name_plural = "User comments"