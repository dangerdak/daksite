from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^blog/',
        include('blog.urls')),

    url(r'^admin/',
        include(admin.site.urls)),
)

# Flatpages
urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/$',
        'flatpage',
        {'url': '/about/'},
        name='about'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
