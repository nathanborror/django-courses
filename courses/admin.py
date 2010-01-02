from django.contrib import admin
from courses.models import *


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Course, CourseAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('title', 'course')
    list_filter   = ('course',)
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Project, ProjectAdmin)


class MilestoneAdmin(admin.ModelAdmin):
    list_display  = ('title', 'project')
    list_filter   = ('project',)
admin.site.register(Milestone, MilestoneAdmin)


class ExampleAdmin(admin.ModelAdmin):
    list_display  = ('title', 'project')
    list_filter   = ('project',)
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Example, ExampleAdmin)


class AssignmentAdmin(admin.ModelAdmin):
    list_display  = ('title', 'course', 'project')
    list_filter   = ('course', 'project')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Assignment, AssignmentAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display  = ('user',)
admin.site.register(Student, StudentAdmin)