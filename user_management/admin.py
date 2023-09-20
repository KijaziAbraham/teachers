from django.contrib import admin
from .models import UserProfile  
from .models import Message 


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'surname', 'gender', 'phone_number', 'level_of_education', 'form_status', 'profile_edited')
    list_filter = ('gender', 'level_of_education')
    search_fields = ('user__username', 'first_name', 'surname', 'phone_number')


class message():
    list_display = ('receiver', 'sender', 'content', 'timestamp')



admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Message)


   

