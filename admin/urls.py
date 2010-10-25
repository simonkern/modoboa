from django.conf.urls.defaults import *

urlpatterns = patterns('modoboa.admin.views',
                       url(r'^$', 'domains', name="index"),
                       url(r'^domains/$', 'domains', name="domains"),
                       (r'^domains/new/', 'newdomain'),
                       (r'^domains/(?P<dom_id>\d+)/edit/$', 'editdomain'),
                       (r'^domains/(?P<dom_id>\d+)/delete/$', 'deldomain'),
                       (r'^domains/(?P<dom_id>\d+)/newmailbox/$', 'newmailbox'),
                       (r'^domains/(?P<dom_id>\d+)/editmailbox/(?P<mbox_id>\d+)/$', 'editmailbox'),
                       (r'^domains/(?P<dom_id>\d+)/deletemailbox/(?P<mbox_id>\d+)/$', 'delmailbox'),
                       (r'^domains/(?P<dom_id>\d+)/newalias/$', 'newalias'),
                       (r'^domains/(?P<dom_id>\d+)/editalias/(?P<alias_id>\d+)/$', 'editalias'),
                       (r'^domains/(?P<dom_id>\d+)/$', 'mailboxes'),
                       (r'^domains/(?P<dom_id>\d+)/raw/$', 'mailboxes_raw'),
                       url(r'^domains/(?P<dom_id>\d+)/aliases/$', "aliases", name="full-aliases"),
                       url(r'^domains/(?P<dom_id>\d+)/aliases/(?P<mbox_id>\d+)/$', "aliases", name="mbox-aliases"),
                       (r'^domains/(?P<dom_id>\d+)/delalias/(?P<alias_id>\d+)/$', 'delalias'),
                       (r'^settings/$', 'settings'),
                       (r'^settings/addperm/$', 'addpermission'),
                       (r'^settings/delperm/(?P<mbox_id>\d+)/(?P<group>\w+)/$', 'deletepermission'),
                       (r'^settings/parameters/$', 'viewparameters'),
                       (r'^settings/parameters/save/$', 'saveparameters'),
                       (r'^settings/extensions/$', 'viewextensions'),
                       (r'^settings/extensions/save/$', 'saveextensions'),
                       )
