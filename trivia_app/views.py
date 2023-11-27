from typing import Any
from django.shortcuts import render,redirect
from django.http import HttpResponse


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.forms import CardForm, CardDeckForm
from django.contrib import messages

from trivia_app.models import User, CardDeck, Card
from trivia_app.forms import UserForm, CardDeckForm, CardForm

#From https://learndjango.com/tutorials/django-signup-tutorial
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)



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
  # template_name = 'trivia_app/carddeck_detail.html'
   
   #From https://stackoverflow.com/questions/41287431/django-combine-detailview-and-listview
   def get_context_data(self, *args, **kwargs):
      context =super(UserDetailView, self).get_context_data(*args, **kwargs)
      context['carddeck_list'] = CardDeck.objects.all()
      return context



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


#With help of https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/#top
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("create-profile")
    template_name = "registration/signup.html"

class CreateProfileView(generic.CreateView):
   form_class = UserForm
   success_url = reverse_lazy("login")
   template_name = "registration/create-profile.html"

'''
class UpdateCardView(generic.UpdateView):
   form_class = CardForm
   success_url = reverse_lazy("update_card_view")
   template_name = "trivia_app/update_card_view.html"
'''
  
class CardCreate(CreateView):
    model = Card
    fields = [
      'title',
      'question',
      'carddeck',
      'option_1',
      'option_2',
      'option_3',
      'option_4',
      'correct_option',
      ]
    success_url = reverse_lazy('card_list')

class CardDeckCreate(CreateView):
    model = CardDeck
    fields = [
      'title',
      'user',
      'description',
      'is_active',
      'image',
      ]
    success_url = reverse_lazy('carddeck_list')

class UserCreate(CreateView):
    model = User
    fields = [
      'name',
      'about',
      'contact_email',
      ]
    success_url = reverse_lazy('user_list')


class CardUpdate(UpdateView):
   model = Card
   fields = [
      'title',
      'question',
      'carddeck',
      'option_1',
      'option_2',
      'option_3',
      'option_4',
      'correct_option',
   ]
   success_url = reverse_lazy('card_list')

class CardDeckUpdate(UpdateView):
    model = CardDeck
    fields = [
      'title',
      'user',
      'description',
      'is_active',
      'image',
      ]
    success_url = reverse_lazy('carddeck_list')

class UserUpdate(UpdateView):
    model = User
    fields = [
      'name',
      'about',
      'contact_email',
      ]
    success_url = reverse_lazy('user_list')


class CardDelete(DeleteView):
    model = Card
    success_url = reverse_lazy('card_list')

class CardDeckDelete(DeleteView):
    model = CardDeck
    success_url = reverse_lazy('carddeck_list')

class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')























"""
def create_card_view(request):
   context ={}
   # add the dictionary during initialization
   form = CardForm(request.POST or None)
   if form.is_valid():
      form.save()
         
   context['form']= form
   return render(request, "create_card_view.html", context)

def create_carddeck_view(request):
   context ={}
   # add the dictionary during initialization
   form = CardDeckForm(request.POST or None)
   if form.is_valid():
      form.save()
         
   context['form']= form
   return render(request, "create_carddeck_view.html", context)

def create_user_view(request):
   context ={}
   # add the dictionary during initialization
   form = UserForm(request.POST or None)
   if form.is_valid():
      form.save()
         
   context['form']= form
   return render(request, "create_user_view.html", context)




def update_carddeck_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(CardDeck, id = id)
 
    # pass the object as instance in form
    form = CardDeckForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_carddeck_view.html", context)
"""
"""
def update_card_view(self, request, pk):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Card, id = id)
 
    # pass the object as instance in form
    form = CardForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_card_view.html", context)
"""

"""
class UpdateCardView():
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Card, id = id)
 
    # pass the object as instance in form
    form = CardForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_card_view.html", context)
"""

"""
def update_user_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(User, id = id)
 
    # pass the object as instance in form
    form = UserForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_user_view.html", context)
"""