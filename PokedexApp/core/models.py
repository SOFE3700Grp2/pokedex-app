from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag (models.Model):
    tag = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.tag

class Image (models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pic = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    tags = models.ManyToManyField(Tag)
    public = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Message(models.Model):
    """
    """

    text= models.CharField(max_length=250)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s at %s" % (self.sender, self.date)

class Comment(models.Model):
    """
    """

    text = models.CharField(max_length=1000)
    posted_on = models.DateField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.ForeignKey(Image, on_delete=models.CASCADE)
    def __str__(self):
        return "%s on %s" % (self.posted_by, self.about)
