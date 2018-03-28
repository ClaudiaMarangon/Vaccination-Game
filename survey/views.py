from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Strategy(Page):
    form_model = models.Player
    form_fields = ['two_p', 'three_p']
    pass

class Survey_Extract1(Page):
    form_model = models.Player
    form_fields = ['q1', 'q2', 'q3']
    pass

class Survey_Extract2(Page):
    form_model = models.Player
    form_fields = ['q4', 'q5', 'q6', 'q7', 'q8']
    pass


class Survey_Extract3(Page):
    form_model = models.Player
    form_fields = ['doc', 'par', 'fre', 'med', 'tv', 'oth', 'spec']
    pass


page_sequence = [
    Strategy,
    Survey_Extract1,
    Survey_Extract2,
    Survey_Extract3
]
