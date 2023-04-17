"""
URL configuration for chat project.

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
from chatApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignUpView.as_view()),
    path('signin/', views.SignInView.as_view()),
    path('create/', views.CreateView.as_view()),
    path('thread/delete/<int:thread_id>/', views.DeleteThreadView.as_view()),
    path('thread/list/<int:user_id>/', views.ThreadsListView.as_view()),
    path('message/create/', views.CreateMessageView.as_view()),
    path('message/list/<int:thread_id>/', views.MessagesInThreadView.as_view()),
    path('message/read/<int:message_id>/', views.MessageReadView.as_view()),
    path('message/unread/<int:user_id>/', views.UnreadMessageNumberView.as_view())
]
