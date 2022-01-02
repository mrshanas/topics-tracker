from django.urls import path,include
from . import views
# for the home page
# from django.conf.urls import url


#Create your urls here.

app_name = 'topics'

urlpatterns = [
    # Home page
    # url(r'^$',views.index,name='index'),
    path('',views.home_page,name='home_page'),
    path('topics',views.topics_list,name='topics_list'),
    path('<int:topic_id>/',views.topic,name='topic'),
    # for adding a new topic
    path('new_topic/',views.new_topic,name='new_topic'),
    # adding a new entry
    path('<int:topic_id>/new_entry',views.new_entry,name='new_entry'),
    # editing a new entry
    path('<int:entry_id>/edit_entry',views.edit_entry,name='edit_entry'),
    # deleting an entry
    path('<int:entry_id>/delete_entry',views.delete_entry,name='delete_entry'),
    # deleting a topic
    path('<int:topic_id>/delete_topic',views.delete_topic,name='delete_topic')
]