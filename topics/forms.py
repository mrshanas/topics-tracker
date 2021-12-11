from django import forms
from .models import Topic,Entry

#Create your forms here.

class TopicForm(forms.ModelForm):
    """Allow user add new topics"""
    class Meta:
        model = Topic
        fields = ['title']
        labels = {'title':""}

class EntryForm(forms.ModelForm):
    """Allow user add new entries"""
    class Meta:
        model = Entry
        fields = ['body']
        labels = {'body':""}