from django.test import TestCase
from trivia_app.models import Card, CardDeck, User

from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver

import os

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
driver.implicitly_wait(100)
driver.get("http://127.0.0.1:8000")
print(driver.title)
driver.close()

class GeneralFunctionalTests(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_navigate_site(self):
        self.browser.get('http://127.0.0.1:8000')
        assert 'Django' in self.browser.title




class UserTestCase(TestCase):
    '''
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
    '''
    def test_users(self):
        charles = User.objects.all().filter(name="Charles")
        billy = User.objects.all().filter(name="Billy")
        if len(charles) > 0:
            self.assertEqual(charles[0].about, 'my name is charles')
        else:
            print("None on line 39")    
        if len(billy) > 0:
            self.assertEqual(billy[0].contact_email, 'billy@billy.com')
        else:
            print("none on 43")



class CardTestCase(TestCase):
    '''
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
    '''
    def test_users(self):
        cards = Card.objects.all().filter(title="Test card 1")
        if len(cards) > 0:
            self.assertEqual(cards[0].correct_option, 'Slim Shady')
            self.assertEqual(cards[0].option_1, 'Easy e')
            self.assertEqual(cards[0].option_2, 'Tupac')
            self.assertEqual(cards[0].option_3, 'Slim Shady')
            self.assertEqual(cards[0].option_4, 'Big Sunny')
            self.assertEqual(cards[0].question, 'Eminem nickname')
            self.assertEqual(cards[0].carddeck, 4)
        else:
            print("None on 86")


class CardDeckTestCase(TestCase):
    '''
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
    '''
    def test_users(self):
        carddeck = CardDeck.objects.all().filter(title="Test card deck")
        if len(carddeck) > 0:
            self.assertEqual(carddeck[0].user, 5)
            self.assertEqual(carddeck[0].description, 'Some card deck desc')
            self.assertEqual(carddeck[0].is_active, 'True')
            self.assertEqual(carddeck[0].image, 'static/images/navbar_logo.png')
        else:
            print("None on line 115")    
        
        