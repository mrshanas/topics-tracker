from django.urls import path,include
from . import views
# for the home page
# from django.conf.urls import url


#Create your urls here.

app_name = 'topics'

urlpatterns = [
    # Home page
    # url(r'^$',views.index,name='index'),
    path('',views.topics_list,name='topics_list'),
    path('<int:topic_id>/',views.topic,name='topic'),
]