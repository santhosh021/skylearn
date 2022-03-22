from django.contrib import admin
from . import models

# Register your models here.


class VideosAdmin(admin.StackedInline):
    model = models.Videos

class Lecture(admin.ModelAdmin):
    inlines = [VideosAdmin]


admin.site.register(models.Course, Lecture)
admin.site.register(models.Videos)
