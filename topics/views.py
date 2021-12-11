from django.http import request
from django.shortcuts import render
from .models import Topic,Entry
from .forms import EntryForm, TopicForm

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

def new_topic(request):
    """Enables user to add a new topic"""
    if request.method == 'POST':
        new_topic = TopicForm(request.POST)

        if new_topic.is_valid():
            new_topic.save()
            new_topic_data = new_topic.cleaned_data
            print("Success")
            print(new_topic_data)
        else:
            print("Failure")

    else:
        new_topic = TopicForm()

    return render(request,'topics/new_topic.html',{'new_topic':new_topic})


def new_entry(request,topic_id):
    """Adding entries to specific topics"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        entry_form = EntryForm()

    else:
        entry_form = EntryForm(request.POST)

        if entry_form.is_valid():
            # save the entry to the database
            form = entry_form.save(commit=False)
            form.topic = topic
            form.save()

    return render(request,'topics/new_entry.html',{'entry_form':entry_form,'topic':topic})

def edit_entry(request,entry_id):
    """Editing the existing entries"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # pre-fill the form with previous entry
        form = EntryForm(instance=entry)
    else:
        # edited and submitted form
        form = EntryForm(instance=entry,data=request.POST)

        if form.is_valid():
            form.save()

    context = {'entry':entry,'form':form,'topic':topic}
    return render(request,'topics/edit_entry.html',context)