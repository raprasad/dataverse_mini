from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.dataverses.views',
    url(r'^show/$', 'show_dataverses', name="show_dataverses"),
    
)
