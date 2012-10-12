from django.conf.urls import patterns, include, url
from filebrowser.sites import site
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from blog.api import PostResource

admin.autodiscover()
entry_resource = PostResource()
urlpatterns = patterns('home.views',
       (r'^$', 'main'),
       
        )
urlpatterns += patterns('blog.views',
      (r'^blog$', 'main'),
      
        (r"^add_comment/(\d+)/$", "add_comment"),
        (r"^month/(\d+)/(\d+)/$", "month"),
        (r"^delete_comment/(\d+)/$", "delete_comment"),
        (r"^delete_comment/(\d+)/(\d+)/$", "delete_comment"),
        (r'^([\w-]+).html$', 'post'),
      
        )

urlpatterns += patterns('page.views',
       (r'^page$', 'main'),
      
        (r"^page/add_comment/(\d+)/$", "add_comment"),
        (r"^page/month/(\d+)/(\d+)/$", "month"),
        (r"^page/delete_comment/(\d+)/$", "delete_comment"),
        (r"^page/delete_comment/(\d+)/(\d+)/$", "delete_comment"),
        (r'^([\w-]+)$', 'post'),
      
        )
urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    url(r'^demo/','django.views.generic.simple.direct_to_template',{'template':'demo.html'}),
    url(r'^api/', include(entry_resource.urls)),
)


