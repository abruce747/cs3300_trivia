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
    #path('update_card_view/',views.update_card_view,name='update_card_view'),
    #path('cards/<int:pk>/update_card_view/',views.UpdateCardView.as_view(),name='update_card_view'),
   

    #From https://medium.com/@20ce125/django-crud-create-retrieve-update-delete-operations-441a8a296119
    path('new_card', views.CardCreate.as_view(), name='new_card'),
    path('new_carddeck', views.CardDeckCreate.as_view(), name='new_carddeck'),
    path('new_user', views.UserCreate.as_view(), name='new_user'),
    path('edit_card/<int:pk>', views.CardUpdate.as_view(), name='edit_card'),
    path('edit_carddeck/<int:pk>', views.CardDeckUpdate.as_view(), name='edit_carddeck'),
    path('edit_user/<int:pk>', views.UserUpdate.as_view(), name='edit_user'),
    path('delete_card/<int:pk>', views.CardDelete.as_view(), name='delete_card'),
    path('delete_carddeck/<int:pk>', views.CardDeckDelete.as_view(), name='delete_carddeck'),
    path('delete_user/<int:pk>', views.UserDelete.as_view(), name='delete_user'),



]

