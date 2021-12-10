from django.http import request
from django.shortcuts import render
from .models import Topic,Entry

# from django.shortcuts import get_object_or_404

# Create your views here.
# the password is 'moodle'

def topics_list(request):
    """Display the user's topics"""
    # the negative sign sorts the topic by currently
    topics = Topic.objects.order_by('-date_added')

    return render(request,'topics/topics.html',{'topics':topics})

def topic(request,topic_id):
    """Display each individual topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')

    return render(request,'topics/topic.html',{'topic':topic,'entries':entries})
