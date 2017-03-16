from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kwons.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/$',views.index,name='index'),
    url(r'^polls/(?P<question_id>\d+)/$)',views.detail, name='detail'),
    url(r'^polls/(?P<question_id>\d+)/vote/$',views.vote, name='vote'),
    url(r'^polls/(?P<question_id>\d+)/results/$',views.results, name='results'),
    url(r'^admin/',include(admin.site.urls)),
)
