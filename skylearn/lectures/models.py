from django.db import models

# Create your models here.
class Lecture(models.Model):
    lec_name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, default='', unique=True, primary_key=True)
    lec_image = models.ImageField(upload_to ='static/images/uploads/')
    lec_description = models.TextField(null=True)

    def __str__(self):
        return self.slug

class LectureDetail(models.Model):
    title = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    topic = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, default='')
    description = models.TextField()

    def __str__(self):
        return self.topic
