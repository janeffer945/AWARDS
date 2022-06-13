from django.urls import path
from django.contrib import admin
from ratings import views
urlpatterns=[
    path('api/projects/', views.ProjectList.as_view()),
    path('api/profiles/',views.ProfileList.as_view())
    
]