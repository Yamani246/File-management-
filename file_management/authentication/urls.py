from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profile',views.userprofile,name='userprofile'),
    path('',views.login_,name='login_'),
    path('upload_file',views.upload,name='upload'),
    path('viewpage',views.viewpage,name='viewpage'),
    path('view_file',views.viewfile,name='viewfile'),
    path('<path:filename>/download/', views.download, name='download'),
    path('logout',views.logout_,name='logout_'),
]
