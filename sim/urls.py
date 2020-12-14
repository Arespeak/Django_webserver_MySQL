from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^content/$', views.content),
    url(r'^index/$', views.index),
    url(r'^add/$', views.add),
    url(r'^edit/$', views.edit),
    url(r'^delete/$', views.delete),
    url(r'^find/$', views.find),
    url(r'^v_index/$', views.v_index),
    url(r'^v_add/$', views.v_add),
    url(r'^v_edit/$', views.v_edit),
    url(r'^v_delete/$', views.v_delete),
    url(r'^v_find/$', views.v_find),
    url(r'^sign_up/$', views.sign_up),
    url(r'^u_index/(?P<u_id>\w+)/$', views.u_index, name='id_index'),
    url(r'^view_others/(?P<u_id>\w+)/$', views.view_others, name='others'),
    url(r'^search_others/(?P<u_id>\w+)/(?P<v_id>\w+)/$', views.search_others, name='search'),
    url(r'^likes/(?P<u_id>\w+)/$', views.likes),
    url(r'^follows/(?P<u_id>\w+)/$', views.follows),
    url(r'^u_delete/$', views.u_delete),
    url(r'^u_v_add/$', views.u_v_add),
    url(r'^u_edit/$', views.u_edit),
    url(r'^login_1/$', views.login_1),
]