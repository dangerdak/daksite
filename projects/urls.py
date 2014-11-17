from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from projects import views

urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(template_name='projects/projects.html'),
        name='project_list'),

    url(r'^ajax_countries/$',
        views.ajax_countries,
        name='ajax_countries'),
)
