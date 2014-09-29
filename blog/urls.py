from django.conf.urls import patterns, url

from blog.views import PostListView

urlpatterns = patterns('',
    # Index view
    url(r'^$',
        PostListView.as_view(),
        name='post_list',
        ),
)
