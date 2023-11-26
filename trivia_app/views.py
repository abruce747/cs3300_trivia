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
   active_carddecks = CardDeck.objects.all().filter(is_active='True')  
   return render( request, 'trivia_app/index.html', {'carddeck_list':active_carddecks})

def cards(request):
   associated_cards = Card.objects.all()
   print("/n/nAssociated cards===============/n")
   print(associated_cards)
   print("/n/n")
   return render(request, 'trivia_app/card_list.html', {'card_list':associated_cards})

def users(request):
   user_list = User.objects.all()
   return render(request, 'trivia_app/user_list.html', {'user_list':user_list})



class UserListView(generic.ListView):
   model = User

class UserDetailView(generic.DetailView):
   model = User



class CardDeckDetailView(generic.DetailView):
   model = CardDeck
   def display(request):
      all_cards = Card.objects.all()
      print("/n/nAssociated cards===============/n")
      print(all_cards)
      print("/n/n")
      return render(request, 'trivia_app/card_list.html', {'card_list':all_cards})



class CardDeckListView(generic.ListView):
   model = CardDeck




class CardDetailView(generic.DetailView):
   model = Card

class CardListView(generic.ListView):
   model = Card