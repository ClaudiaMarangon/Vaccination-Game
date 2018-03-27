from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Instructions(Page):
    def is_displayed(self):
        return self.round_number==1
    pass

class Probability(Page):
    form_model = models.Player
    form_fields = ['prob']
    pass

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Instructions,
    Probability,
    MyPage,
    ResultsWaitPage,
    Results
]
