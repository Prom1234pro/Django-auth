import site
from django.contrib import admin

from course.models import Course, User

# Register your models here.
admin.site.register(User)
admin.site.register(Course)