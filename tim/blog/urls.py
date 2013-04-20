from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tim.views.home', name='home'),
    # url(r'^tim/', include('tim.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^$',views.index),
     url(r'^api/posts',views.index_json),
     url(r'^posts/(\d+)/?',views.display_post),
     url(r'^tags/([A-Za-z0-9_-]+)/?',views.display_tag),
)
