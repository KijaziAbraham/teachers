from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm  
from .forms import UserProfileForm
from .forms import UserProfile
from .models import UserProfile 
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db import IntegrityError
from .models import Message 

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                user_profile = UserProfile.objects.get(user=user)
                if user_profile.form_status == 1:
                    return redirect('user_management:profile_view')
                elif user_profile.form_status == 0:
                    return redirect('user_management:adding_informations')
    else:
        form = AuthenticationForm()
    return render(request, 'user_management/login.html', {'form': form})


def registration_view(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            user_profile = UserProfile.objects.create(user=user)
            return redirect('user_management:login_view')  
    else:
        form = CustomRegistrationForm()
    return render(request, 'user_management/registration.html', {'form': form})

  
@login_required
def adding_informations_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            # Save the user's profile information
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.form_status = 1
            user_profile.save()

            return redirect('user_management:profile_view')

    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'user_management/adding_informations.html', {'form': form})



def home_view(request):
    return render(request, 'user_management/home.html')


@login_required
def profile_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        return redirect('user_management:profile_view')

    return render(request, 'user_management/profile_view.html', {'user_profile': user_profile})

@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            # Save the updated profile
            form.save()

            # Update the profile_edited flag to prevent further edits
            user_profile.profile_edited = True
            user_profile.save()

            messages.success(request, "You have successfully edited your profile.")
            return redirect('user_management:profile_view')
        else:
            messages.error(request, "There was an error in your profile edit. Please check the form.")
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'user_management/profile_view.html', {'user_profile': user_profile, 'form': form})


# @login_required
# def notification_view(request):
#     user_profiles = UserProfile.objects.all()

#     for user_profile1 in user_profiles:
#         for user_profile2 in user_profiles:
#             if (
#                 user_profile1.district_council_preference == user_profile2.council_currently_working and
#                 user_profile1.council_currently_working == user_profile2.district_council_preference
#             ):
#                 # Users match, add a success message for both users
#                 messages.success(request, f"You have been matched with {user_profile1.user.username}. Please contact US to arrange a location swap.") 


#     return render(request, 'user_management/notification.html')



@login_required
def view_messages(request):
    # Retrieve messages or swap requests for the logged-in teacher
    messages =Message.objects.filter(receiver=request.user)

    # You can customize this query to get the messages or swap requests you need

    return render(request, 'user_management/notification.html', {'messages': messages})


