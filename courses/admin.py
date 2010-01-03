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


class ProjectMilestoneAdmin(admin.ModelAdmin):
    list_display  = ('title', 'project')
    list_filter   = ('project',)
admin.site.register(ProjectMilestone, ProjectMilestoneAdmin)


class ProjectExampleAdmin(admin.ModelAdmin):
    list_display  = ('title', 'project')
    list_filter   = ('project',)
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(ProjectExample, ProjectExampleAdmin)


class AssignmentAdmin(admin.ModelAdmin):
    list_display  = ('title', 'course', 'project')
    list_filter   = ('course', 'project')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Assignment, AssignmentAdmin)