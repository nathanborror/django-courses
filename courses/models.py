import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models import permalink


class AbstractModel(models.Model):
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

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')

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
    start = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())
    due = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        ordering = ['start']

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('courses:project', None, {
            'course_slug': self.course.slug,
            'slug': self.slug
        })


class ProjectMilestone(AbstractModel):
    """ Project milestone model """
    project = models.ForeignKey(Project, related_name='milestones')
    title = models.CharField(blank=True, max_length=255)
    due = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())

    class Meta:
        verbose_name = _('project milestone')
        verbose_name_plural = _('project milestones')
        ordering = ['due']

    def __unicode__(self):
        return self.title


def get_example_image_path(instance, filename):
    import os.path, hashlib
    name = hashlib.md5(instance.title).hexdigest()
    ext = os.path.splitext(filename)
    return os.path.join('examples', '%s%s' % (name, ext[1]))

class ProjectExample(AbstractModel):
    """ Project example model """
    project = models.ForeignKey(Project, related_name='examples')
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.FileField(blank=True, upload_to=get_example_image_path)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = _('project example')
        verbose_name_plural = _('project examples')

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('courses:project_example', None, {
            'course_slug': self.project.course.slug,
            'slug': self.project.slug,
            'object_id': self.pk
        })

    def get_previous(self):
        return self.get_previous_by_created(project=self.project)

    def get_next(self):
        return self.get_next_by_created(project=self.project)


ASSIGNMENT_TYPES = (
    (0, 'Reading'),
    (1, 'Watching'),
    (2, 'Listening'),
    (3, 'Writing')
)

class Assignment(AbstractModel):
    """ Assignment model """
    course = models.ForeignKey(Course, related_name='assignments')
    project = models.ForeignKey(Project, blank=True, null=True, related_name='assignments', help_text="If assignment is related to a project.")
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    assignment_type = models.PositiveSmallIntegerField(choices=ASSIGNMENT_TYPES, blank=True, null=True)
    description = models.TextField(blank=True)
    start = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())
    due = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())

    class Meta:
        verbose_name = _('assignment')
        verbose_name_plural = _('assignments')
        ordering = ['start']

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('courses:assignment', None, {
            'course_slug': self.course.slug,
            'slug': self.slug
        })