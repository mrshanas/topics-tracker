from django.http import request
from django.shortcuts import redirect, render
from .models import Topic,Entry
from .forms import EntryForm, TopicForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# from django.shortcuts import get_object_or_404

# Create your views here.
# the password is 'moodle'

def home_page(request):
    return render(request,'topics/index.html')

@login_required
def topics_list(request):
    """Display the user's topics"""
    # the negative sign sorts the topic by currently
    
    # possessing a topic to a specific user
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')

    return render(request,'topics/topics.html',{'topics':topics})
@login_required
def topic(request,topic_id):
    """Display each individual topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')

    if topic.owner != request.user:
        raise Http404

    return render(request,'topics/topic.html',{'topic':topic,'entries':entries})

@login_required
def new_topic(request):
    """Enables user to add a new topic"""
    if request.method == 'POST':
        new_topic = TopicForm(request.POST)

        if new_topic.is_valid():
            new_topic_form = new_topic.save(commit=False)
            new_topic_form.owner = request.user
            new_topic_form.save()
            # print("Success")
            return redirect('topics:topics_list')
     

    else:
        new_topic = TopicForm()

    return render(request,'topics/new_topic.html',{'new_topic':new_topic})

@login_required
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
            return redirect('topics:topics_list')

    return render(request,'topics/new_entry.html',{'entry_form':entry_form,'topic':topic})

@login_required
def edit_entry(request,entry_id):
    """Editing the existing entries"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

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