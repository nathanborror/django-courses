from django.conf.urls.defaults import *


urlpatterns = patterns('courses.views',
    url(r'^$',
        view='course_list',
        name='courses'),

    url(r'^(?P<course_slug>[-\w]+)/$',
        view='course_detail',
        name='course'),

    url(r'^(?P<course_slug>[-\w]+)/students/$',
        view='course_student_list',
        name='course_students'),

    url(r'^(?P<course_slug>[-\w]+)/projects/$',
        view='project_list',
        name='projects'),

    url(r'^(?P<course_slug>[-\w]+)/projects/(?P<slug>[-\w]+)/$',
        view='project_detail',
        name='project'),

    url(r'^(?P<course_slug>[-\w]+)/projects/(?P<slug>[-\w]+)/examples/(?P<object_id>\d+)/$',
        view='project_example_detail',
        name='project_example'),

    url(r'^(?P<course_slug>[-\w]+)/projects/(?P<slug>[-\w]+)/examples/$',
        view='project_example_list',
        name='project_examples'),

    url(r'^(?P<course_slug>[-\w]+)/projects/(?P<slug>[-\w]+)/assignments/$',
        view='project_assignment_list',
        name='project_assignments'),

    url(r'^(?P<course_slug>[-\w]+)/assignments/$',
        view='assignment_list',
        name='assignments'),

    url(r'^(?P<course_slug>[-\w]+)/assignments/(?P<slug>[-\w]+)/$',
        view='assignment_detail',
        name='assignment'),
)