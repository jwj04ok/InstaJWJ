from django.contrib import admin

# Register your models here.
from testapp1.models import Post, InstaUser, Like, UserConnection
 

admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(Like)
admin.site.register(UserConnection)