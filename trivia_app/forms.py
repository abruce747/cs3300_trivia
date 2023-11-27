from django import forms
from .models import Card, CardDeck, User

#Lots of help from https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = [
            "title",
            "question",
            "carddeck",
            "option_1",
            "option_2",
            "option_3",
            "option_4",
            "correct_option",
        ]


class CardDeckForm(forms.ModelForm):
    class Meta:
        model = CardDeck
        fields = [
            "title",
            "user",
            "description",
            "is_active",
            "image",
        ]



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "name",
            "about",
            "contact_email",
        ]

