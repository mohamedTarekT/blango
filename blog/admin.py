from django.contrib import admin
from blog.models import Tag, Post,Comment
from django.contrib import admin


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    list_display = ['value']



admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
