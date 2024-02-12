"""
URL configuration for mini project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miniapp import views

'''
urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.LandingBeforeLogin, name='LandingBeforeLogin'),
    path('Signup.html', views.Signup, name='Signup'),
    
    path('Login.html', views.Login, name='Login'),
    path('Profile.html',views.Profile, name='Profile'),
    path('LandingAfterLogin.html',views.LandingAfterLogin, name='LandingAfterLogin'),
    path('About.html',views.About, name='About'),
    path('Courses.html',views.Courses, name='Courses'),
    path('Pythoncourse.html',views.Pythoncourse, name='Pythoncourse'),
    path('Javacourse.html',views.Javacourse, name='Javacourse'),
    path('Cppcourse.html',views.Cppcourse, name='Cppcourse'),
    path('Profile.html',views.Profile, name='Profile'),
    path('Contact.html',views.Contact, name='Contact'),
    path('Dashboard.html',views.Dashboard, name='Dashboard'),
]

'''


urlpatterns = [
    # Other URL patterns
    path('', views.index),
    path('api/signup/', views.signup, name='signup'),
    path('api/login/', views.login, name='login'),
    #path('api/profile/', views.Profile, name='profile'),
    path('api/submit_survey/', views.submit_survey, name='submit_survey'),
    path('api/predict/',views.predict, name='predict'),
]

