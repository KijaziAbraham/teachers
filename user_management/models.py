from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default=" ")
    middle_name = models.CharField(max_length=50, blank=True, null=True, default=" ")
    surname = models.CharField(max_length=50, default=" ")
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    LEVEL_OF_EDUCATION_CHOICES = (
         ('PRIMARY SCHOOL', 'PRIMARY SCHOOL'),
         ('SECONDARY SCHOOL', 'SECONDARY SCHOOL'),  
    )
    #form_status values
    #0 = no value found
    #1 = value found
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=" ")
    phone_number = models.CharField(max_length=15, default=" ")
    level_of_education = models.CharField(max_length=50, choices=LEVEL_OF_EDUCATION_CHOICES, default=" ")
    school_currently_teaching = models.CharField(max_length=100, default=" ")
    council_currently_working = models.CharField(max_length=100, default=" ")
    district_council_preference = models.CharField(max_length=100, default=" ")
    first_subject_major = models.CharField(max_length=50, default=" ")
    second_subject = models.CharField(max_length=50, blank=True, null=True, default=" ")
    form_status = models.IntegerField( default='0')
    profile_edited = models.BooleanField(default=False) 


def __str__(self):
        return f"{self.user.username}'s Profile"



class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username}: {self.content}"
