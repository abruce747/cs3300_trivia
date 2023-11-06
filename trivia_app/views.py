from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
#from django.forms import CardForm, CardDeckForm
from django.contrib import messages

from trivia_app.models import User, CardDeck, Card


# Create your views here.
"""
def index(request):
# Render the HTML template index.html with the data in the context variable.
   #Replaced:
   #return HttpResponse('home page')
   #with:
   return render( request, 'trivia_app/index.html')
"""

def index(request):
   #Need to fix the is_active issue.
   #user_active_carddecks = User.objects.select_related('carddeck').all().filter(carddeck__is_active='True')
   user_active_carddecks = User.objects.select_related('carddeck').all()
   #print("active portfolio query set", user_active_carddecks)
   return render( request, 'trivia_app/index.html', {'user_active_carddecks':user_active_carddecks})


class UserListView(generic.ListView):
   model = User

class UserDetailView(generic.DetailView):
   model = User

class CardDeckDetailView(generic.DetailView):
   model = CardDeck

class CardDeckListView(generic.ListView):
   model = CardDeck

class CardDetailView(generic.DetailView):
   model = Card

class CardListView(generic.ListView):
   model = Card