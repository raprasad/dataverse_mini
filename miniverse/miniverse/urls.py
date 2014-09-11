from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geoconnect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dv/', include('apps.dataverses.urls')),

    (r'^miniverse-admin//doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^miniverse-admin/', include(admin.site.urls)),
    
) 

# Uncomment the next line to serve media files in dev.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
