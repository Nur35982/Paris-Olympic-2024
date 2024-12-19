from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import signup_view
from .views import booking_view



urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events_list, name='events_list'),
    path('athletes/', views.athletes_list, name='athletes_list'),
    path('stories/', views.stories, name='stories'),
    path('results/', views.results, name='results'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('booking/', booking_view, name='booking'),
    
]
