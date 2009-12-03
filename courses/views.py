from django.shortcuts import get_object_or_404
from django.views.generic import date_based, list_detail

from nathanborror.apps.courses.models import *


def course_list(request, **kwargs):
    return list_detail.object_list(
        request,
        queryset=Course.objects.all(),
        template_object_name='course',
        **kwargs
    )


def course_detail(request, course_slug, **kwargs):
    return list_detail.object_detail(
        request,
        queryset=Course.objects.all(),
        slug=course_slug,
        template_object_name='course',
        **kwargs
    )


def course_student_list(request, course_slug, **kwargs):
    course = get_object_or_404(Course, slug=course_slug)
    return list_detail.object_list(
        request,
        queryset=Student.objects.filter(courses=course),
        template_object_name='student',
        extra_context = {'course': course},
        **kwargs
    )


def project_list(request, course_slug, **kwargs):
    course = get_object_or_404(Course, slug=course_slug)
    return list_detail.object_list(
        request,
        queryset=Project.objects.filter(course=course),
        template_object_name='project',
        extra_context = {'course': course},
        **kwargs
    )


def project_detail(request, course_slug, slug, **kwargs):
    course = get_object_or_404(Course, slug=course_slug)
    return list_detail.object_detail(
        request,
        queryset=Project.objects.filter(course=course),
        slug=slug,
        template_object_name='project',
        extra_context = {'course': course},
        **kwargs
    )


def project_example_list(request, course_slug, slug, **kwargs):
    course = get_object_or_404(Course, slug=course_slug)
    project = get_object_or_404(Project, slug=slug)
    return list_detail.object_list(
        request,
        queryset=Example.objects.filter(project=project),
        template_object_name='example',
        extra_context = {
            'course': course,
            'project': project
        },
        **kwargs
    )


def project_assignment_list(request, course_slug, slug, **kwargs):
    course = get_object_or_404(Course, slug=course_slug)
    project = get_object_or_404(Project, slug=slug)
    return list_detail.object_list(
        request,
        queryset=Assignment.objects.filter(project=project),
        template_object_name='assignment',
        extra_context = {
            'course': course,
            'project': project
        },
        **kwargs
    )


def assignment_list(request, course_slug, **kwargs):
    course = get_object_or_404(Course, slug=course_slug)
    return list_detail.object_list(
        request,
        queryset=Assignment.objects.filter(course=course),
        template_object_name='assignment',
        extra_context = {'course': course},
        **kwargs
    )


def assignment_detail(request, course_slug, slug, **kwargs):
    course = get_object_or_404(Course, slug=course_slug)
    return list_detail.object_detail(
        request,
        queryset=Assignment.objects.filter(course=course),
        slug=slug,
        template_object_name='assignment',
        extra_context = {'course': course},
        **kwargs
    )