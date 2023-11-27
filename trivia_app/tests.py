from django.test import TestCase
from trivia_app.models import Card, CardDeck, User

from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) browser.implicitly_wait(5)


class UserTestCase(TestCase):
    def setUp(self):
        test_user_1 = User(
            name="Charles", 
            about="my name is charles",
            contact_email="charles@google.com"
        )
        test_user_1.save()
        test_user_2 = User(
            name="Billy",
            about="eijthsi billy about me",
            contact_email="billy@billy.com"
        )
        test_user_2.save()

    def test_users(self):
        charles = User.objects.get(name="Charles")
        billy = User.objects.get(name="Billy")
        self.assertEqual(charles.about, 'my name is charles')
        self.assertEqual(billy.contact_email, 'billy@billy.com')


class CardTestCase(TestCase):
    user_inst = User(
        name = "first last",
        about = "bio desc",
        contact_email = "some@yahoo.com"
    )
    user_inst.save()
    carddeck_inst = CardDeck(
        title="deck title",
        user = user_inst,
        description = "something to describe",
        is_active = True,
        image = "static/images/navbar_logo.png"
    )
    carddeck_inst.save()
    def setUp(self):
        Card.objects.create(
            title="Test card 1", 
            question="Eminem nickname",
            carddeck=CardTestCase.carddeck_inst,
            option_1="Easy e",
            option_2="Tupac",
            option_3="Slim Shady",
            option_4="Big Sunny",
            correct_option="Slim Shady"
        )

    def test_users(self):
        cards = Card.objects.get(title="Test card 1")
        self.assertEqual(cards.correct_option, 'Slim Shady')
        self.assertEqual(cards.option_1, 'Easy e')
        self.assertEqual(cards.option_2, 'Tupac')
        self.assertEqual(cards.option_3, 'Slim Shady')
        self.assertEqual(cards.option_4, 'Big Sunny')
        self.assertEqual(cards.question, 'Eminem nickname')
        self.assertEqual(cards.carddeck, CardTestCase.carddeck_inst)



class CardDeckTestCase(TestCase):
    user_inst = User(
        name = "first last",
        about = "bio desc",
        contact_email = "some@yahoo.com"
    )
    user_inst.save()
    def setUp(self):
        CardDeck.objects.create(
            title="Test card deck", 
            user=CardDeckTestCase.user_inst,
            description="Some card deck desc",
            is_active="True",
            image="static/images/navbar_logo.png"
        )

    def test_users(self):
        carddeck = CardDeck.objects.get(title="Test card deck")
        self.assertEqual(carddeck.user, CardDeckTestCase.user_inst)
        self.assertEqual(carddeck.description, 'Some card deck desc')
        self.assertEqual(carddeck.is_active, 'True')
        self.assertEqual(carddeck.image, 'static/images/navbar_logo.png')
       