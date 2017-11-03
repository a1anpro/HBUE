from django.contrib import admin

from .models import *

# Register your models here.

class ClsstAdmin(admin.ModelAdmin):
    list_display = ('classId','className')
    search_fields = ('classClass',)
    # fields = ('classId','className')

class CommentAdmin(admin.ModelAdmin):
    fields = ('ifPass',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('clss','teacher','likes','unlikes','commentNum','callRate','passRate','getRate',)
    # search_fields = ('teacherName',)

admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Clss,ClsstAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)
