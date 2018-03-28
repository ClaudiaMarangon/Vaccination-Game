from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Strategy(Page):
    form_model = models.Player
    form_fields = ['two_p', 'three_p']

    pass


page_sequence = [
    Strategy,
]
