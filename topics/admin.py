from django.contrib import admin
from .models import Topic,Entry

# Register your models here.
@admin.register(Topic)
class TopicManager(admin.ModelAdmin):
    
    list_display = ('title','body','date_added')

@admin.register(Entry)
class EntryManager(admin.ModelAdmin):
    list_display = ('topic','date_added','body',)