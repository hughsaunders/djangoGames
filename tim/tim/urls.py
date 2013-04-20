from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import blog

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tim.views.home', name='home'),
    # url(r'^tim/', include('tim.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^blog/', include(blog.urls)),
     url(r'^/?$', RedirectView.as_view(url='/blog')),
)
