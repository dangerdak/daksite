from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from blog.views import PostListView

urlpatterns = patterns('',
    url(r'^$',
        PostListView.as_view(),
        name='post_list'),

    url(r'^admin/',
        include(admin.site.urls)),
)

# Flatpages
urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/$',
        'flatpage',
        {'url': '/about/'},
        name='about'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
