"""
URL configuration for Summarizer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from textsummary import views
from textsummary import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login,name='user_login'),
    path('summarizer_dashboard', views.summarizer_dashboard,name='summarizer_dashboard'),
    path('register', views.register,name='register'),
    path('summarizer_dashboard', views.summarizer_dashboard, name='summarizer_dashboard'), 
    path('summarize/', views.summarize_text, name='summarize_text'),
    path('history', views.history_view, name='history'), 
    path('logout', views.user_logout, name='logout'),
    path('download/word/<int:summary_id>/', views.download_word, name='download_word'),
    path('download/pdf/<int:summary_id>/', views.download_pdf, name='download_pdf'),

]
