from django.urls import path, include
from django.contrib import admin
from . import views
from django.views.generic.base import TemplateView 
from .views import SignUpView, CreateProfileView


urlpatterns = [
    #path function defines a url pattern
    #'' is empty to represent based path to app
    # views.index is the function defined in views.py
    # name='index' parameter is to dynamically create url
    # example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),

    #From https://learndjango.com/tutorials/django-login-and-logout-tutorial
    path('admin/', admin.site.urls),
    #path('accounts/', include('accounts.urls')),  # new
    path('accounts/', include('django.contrib.auth.urls')), 
    
    path('login/', admin.site.login),
    
    path('logout/', admin.site.logout),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('create-profile/', CreateProfileView.as_view(), name='create-profile'),
    

    #From GE05:
    path('users/', views.UserListView.as_view(), name= 'users'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),

    path('carddecks/',views.CardDeckListView.as_view(),name='carddecks'),
    path('carddecks/<int:pk>',views.CardDeckDetailView.as_view(),name='carddeck-detail'),
    #path('carddecks/<int:pk>',views.CardDeckDetailView.post,name='carddeck-detail'),




    path('cards/',views.CardListView.as_view(),name='cards'),
    path('cards/<int:pk>',views.CardDetailView.as_view(),name='card-detail'),

]

