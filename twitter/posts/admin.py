from django.contrib import admin
from . import models


class CommentInLine(admin.TabularInline):
    model = models.Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)
