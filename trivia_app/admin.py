from django.contrib import admin
from .models import User
from .models import Card
from .models import CardDeck

# Register your models here so they can be edited in admin panel
admin.site.register(User)
admin.site.register(Card)
admin.site.register(CardDeck)