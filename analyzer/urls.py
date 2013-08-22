from django.conf.urls import patterns, include, url
from increasing import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'analyzer.views.home', name='home'),
    # url(r'^analyzer/', include('analyzer.foo.urls')),

    
    url(r'^updatePages/', views.updatePages, name='updatePages'),
    url(r'^hosts/$', views.returnInfo, name="returnInfo"),
    url(r'^hosts2/$', views.updateAndReturnInfo, name='updateAndReturnInfo'),
    url(r'^$', views.index, name='index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
