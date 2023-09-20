from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'middle_name',
            'surname',
            'gender',
            'phone_number',
            'level_of_education',
            'school_currently_teaching',
            'council_currently_working',
            'district_council_preference',
            'first_subject_major',
            'second_subject',
        ]
        labels = {
            'first_name': 'First Name',
            'middle_name': 'Middle Name',
            'surname': 'Surname',
            'gender': 'Gender',
            'phone_number': 'Phone Number',
            'level_of_education': 'Level of Education',
            'school_currently_teaching': 'School Currently Teaching',
            'council_currently_working': 'Council Currently Working',
            'district_council_preference': 'District Council Preference',
            'first_subject_major': 'First Subject Major',
            'second_subject': 'Second Subject',
        }
        widgets = {
            'gender': forms.Select(choices=UserProfile.GENDER_CHOICES),
        }


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Enter a valid email address.',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'


class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }




