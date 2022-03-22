from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=256, unique=True)
    course_name_slug = models.SlugField(max_length=256, unique=True, primary_key=True)
    course_image = models.ImageField(upload_to ='static/images/uploads/')

    def __str__(self):
        return self.course_name_slug

class Videos(models.Model):
    video_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=256, unique=True)
    video_name_slug = models.SlugField(max_length=256, default='', unique=True, primary_key=True)
    video_url = models.URLField()
    video_image = models.ImageField(upload_to ='static/images/uploads/')

    def __str__(self):
        return self.video_name_slug
