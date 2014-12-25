from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forkpi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'records.views.login', name='login'),

    url(r'^keypairs$', 'records.views.keypairs', name='keypairs'),
    url(r'^addpair$', 'records.views.addpair', name='addpair'),
    url(r'^editname$', 'records.views.editname', name='editname'),
    url(r'^editpin$', 'records.views.editpin', name='editpin'),
    url(r'^edituid$', 'records.views.edituid', name='edituid'),
    url(r'^deletekeypair$', 'records.views.deletekeypair', name='deletekeypair'),
    url(r'^pdflist$', 'records.views.pdflist', name='pdflist'),

    url(r'^login$', 'records.views.login', name='login'),
    url(r'^loggingin$', 'records.views.loggingin', name='loggingin'),
    
    url(r'^signup$', 'records.views.signup', name='signup'),
    url(r'^adduser$', 'records.views.adduser', name='adduser'),
    
    url(r'^logout$', 'records.views.logout', name='logout'),
)