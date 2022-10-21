from django.urls import path, include
from . import views



app_name = 'user'

urlpatterns = [
    # User URL
    path('join/', views.join, name='join'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('change_password/', views.change_password, name='change_password'),
    path('delete/', views.delete, name='delete'),
    
    #test
    path('googletest/', views.google_social_login, name='google_social_login')
]
