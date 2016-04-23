from django.conf.urls import url
from vote import views

urlpatterns = [
    # ex : /polls/
#    url(r'^index$', views.index,name='index'),
    # ex : /polls/5/
#    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex : /polls/5/results/
#    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex : /polls/5/vote
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^pulish_getcheck/$', views.getcheck, name="getcheck"),
    url(r'^pulish_auditing/$', views.auditing, name="auditing"),
    url(r'^listCategory/$', views.listCategory, name='listCategory'),
    url(r'^readEvent/$', views.readEvent, name='readEvent'),
    url(r'^loadPageHeader/$', views.loadPageHeader, name='loadPageHeader'),
    url(r'^saveChoice/$', views.saveChoice, name='saveChoice'),
    url(r'^queryVoteResult/$', views.queryVoteResult, name='queryVoteResult'),
    
    
]
