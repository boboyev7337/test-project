from django.contrib import admin

from testapi.models import Test, Post, Category

admin.site.register(Test)
admin.site.register(Post)
admin.site.register(Category)
