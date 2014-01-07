from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'votes.views.vote', name='vote'),
    url(r'^results$', 'votes.views.results', name='results'),

    url(r'^admin/', include(admin.site.urls)),
)
