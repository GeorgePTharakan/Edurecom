from django.contrib import admin

# Register your models here.

from .models import UserProfile, Course, QuestionBank, TestResult

admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(QuestionBank)
admin.site.register(TestResult)
