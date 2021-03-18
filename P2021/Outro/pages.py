from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models

class Outro(Page):
    form_model = 'player'
    form_fields = ['e_mail_address']

class Closing(Page):
    pass

page_sequence = [Outro,Closing]
