from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=256, unique=True, primary_key=True)
    category_image = models.ImageField(upload_to ='static/images/uploads/', blank=True)

    def __str__(self):
        return self.category_name

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=256, unique=True, primary_key=True)

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_choice')
    choice = models.CharField(max_length=256)

    def __str__(self):
        return self.choice

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_answer')
    answer = models.CharField(max_length=256)

    def __str__(self):
        return self.answer
