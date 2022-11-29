from django.contrib import admin

# Register your models here.
from .models import Comment, Image, Tag, Message
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Message)
admin.site.register(Comment)



