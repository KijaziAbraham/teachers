from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'user_management'
urlpatterns = [
    path('registration/', views.registration_view, name='registration_view'),
    path('login/', views.login_view, name='login_view'),
    path('', views.home_view, name='home_view'),
    path('adding_informations/', views.adding_informations_view, name='adding_informations'),  
    path('profile_view/', views.edit_profile, name='profile_view'),  
    path('notification/', views.view_messages, name='notification'),      
    ]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



