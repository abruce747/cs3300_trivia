from typing import Any
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
   active_carddecks = CardDeck.objects.all().filter(is_active='True')  
   return render( request, 'trivia_app/index.html', {'carddeck_list':active_carddecks})

def cards(request):
   all_cards = Card.objects.all()
   print("/n/nAll cards===============/n")
   print(all_cards)
   print("/n/n")
   return render(request, 'trivia_app/card_list.html', {'card_list':all_cards})

def users(request):
   user_list = User.objects.all()
   return render(request, 'trivia_app/user_list.html', {'user_list':user_list})



class UserListView(generic.ListView):
   model = User

class UserDetailView(generic.DetailView):
   model = User




class CardDetailView(generic.DetailView):
   model = Card

class CardListView(generic.ListView):
   model = Card



class CardDeckDetailView(generic.DetailView):
   model = CardDeck
  # template_name = 'trivia_app/carddeck_detail.html'
   
   #From https://stackoverflow.com/questions/41287431/django-combine-detailview-and-listview
   def get_context_data(self, *args, **kwargs):
      context =super(CardDeckDetailView, self).get_context_data(*args, **kwargs)
      context['card_list'] = Card.objects.all()
      return context

   """
   all_cards = Card.objects.all()   
   temp_card_list = CardListView()

   #From https://stackoverflow.com/questions/62727762/django-call-custom-function-within-generic-views
   def post(self, request, *args, **kwargs):
      self.object = self.get_object()
      self.display(request)
      return super().post(request, *args, **kwargs)

   def display(request):
      all_cards = Card.objects.all()
      print("/n/nAssociated cards===============/n")
      print(all_cards)
      print("/n/n")
      return render(request, 'trivia_app/card_list.html', {'card_list':all_cards})
   """


class CardDeckListView(generic.ListView):
   model = CardDeck


