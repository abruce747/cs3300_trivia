from django.urls import path
from . import views


urlpatterns = [
    #path function defines a url pattern
    #'' is empty to represent based path to app
    # views.index is the function defined in views.py
    # name='index' parameter is to dynamically create url
    # example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),

    #From GE05:
    path('users/', views.UserListView.as_view(), name= 'users'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),

    path('carddecks/',views.CardDeckListView.as_view(),name='carddecks'),
    path('carddecks/<int:pk>',views.CardDeckDetailView.as_view(),name='carddeck-detail'),
    #path('carddecks/<int:pk>',views.CardDeckDetailView.post,name='carddeck-detail'),




    path('cards/',views.CardListView.as_view(),name='cards'),
    path('cards/<int:pk>',views.CardDetailView.as_view(),name='card-detail'),

]

