from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^vote/', include('vote.urls', namespace="vote")),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_PATH}),
)
