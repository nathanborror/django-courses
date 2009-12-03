from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models import permalink


class AbstractModel(models.Model):
    start_date = models.DateField(auto_now_add=True)
    finish_date = models.DateField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Course(AbstractModel):
    """ Course model """
    code = models.CharField(blank=True, max_length=20)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    goals = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    resources = models.TextField(blank=True)
    evaluation = models.TextField(blank=True)

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')
        db_table = 'courses'
        ordering = ['-start_date']

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('courses:course', None, {'course_slug': self.slug})


class Project(AbstractModel):
    """ Project model """
    course = models.ForeignKey(Course, related_name='projects')
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    goals = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    resources = models.TextField(blank=True)
    evaluation = models.TextField(blank=True)

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        db_table = 'course_projects'
        ordering = ['-start_date']

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('courses:project', None, {
            'course_slug': self.course.slug,
            'slug': self.slug
        })


def get_example_image_path(instance, filename):
    import os.path, hashlib
    name = "%s_%s_%s" % (instance.project.course.pk, instance.project.pk, instance.pk)
    name = hashlib.md5(name).hexdigest()
    ext = os.path.splitext(filename)
    return os.path.join('examples', '%s%s' % (name, ext[1]))

class Example(models.Model):
    """ Example model """
    project = models.ForeignKey(Project, related_name='examples')
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.FileField(upload_to=get_example_image_path)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name = _('example')
        verbose_name_plural = _('examples')
        db_table = 'course_project_examples'

    def __unicode__(self):
        return self.title



ASSIGNMENT_TYPES = (
    (0, 'Reading'),
    (1, 'Watching'),
    (2, 'Listening')
)

class Assignment(AbstractModel):
    """ Assignment model """
    course = models.ForeignKey(Course, related_name='assignments')
    project = models.ForeignKey(Project, blank=True, null=True, related_name='assignments', help_text="If assignment is related to a project.")
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    assignment_type = models.PositiveSmallIntegerField(choices=ASSIGNMENT_TYPES, blank=True, null=True)
    assignment = models.TextField(blank=True)

    class Meta:
        verbose_name = _('assignment')
        verbose_name_plural = _('assignments')
        db_table = 'course_assignment'
        ordering = ['-start_date']

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('courses:assignment', None, {
            'course_slug': self.course.slug,
            'slug': self.slug
        })


class Student(models.Model):
    """ Student model """
    user = models.ForeignKey(User)
    courses = models.ManyToManyField(Course, related_name='students')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('student')
        verbose_name_plural = _('students')
        db_table = 'course_students'

    def __unicode__(self):
        return self.user.get_full_name()


# class Solution(models.Model):
#     """ Solution model """
#     project = models.ForeignKey(Project)
#     student = models.ForeignKey(Student)
#     solution = models.TextField(blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
# 
#     class Meta:
#         verbose_name = _('solution')
#         verbose_name_plural = _('solutions')
#         db_table = 'course_solutions'
# 
#     def __unicode__(self):
#         return '<Solution>'
# 
# 
# class SolutionMedia(models.Model):
#     """ SolutionMedia model """
#     solution = models.ForeignKey(Solution)
#     title = models.CharField(blank=True, max_length=255)
#     slug = models.SlugField()
#     media = models.FileField(upload_to='media')
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
# 
#     class Meta:
#         verbose_name = _('solution media')
#         verbose_name_plural = _('solution media')
#         db_table = 'course_solution_media'
#         order_with_respect_to = 'solution'
# 
#     def __unicode__(self):
#         return '<SolutionMedia>'
