from django.contrib import admin
from . import models

# Register your models here.

class LectureDetailAdmin(admin.StackedInline):
    model = models.LectureDetail

class Lecture(admin.ModelAdmin):
    inlines = [LectureDetailAdmin]

admin.site.register(models.Lecture, Lecture)
admin.site.register(models.LectureDetail)
