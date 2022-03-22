from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)

class ChoiceAdmin(admin.StackedInline):
    model = Choice

class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceAdmin, AnswerAdmin]

admin.site.register(Question, QuestionAdmin)
