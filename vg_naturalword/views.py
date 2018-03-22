from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Probability(Page):
    form_model = models.Player
    form_fields = ['prob']
    pass

class Decision(Page):
    form_model = models.Player
    form_fields = ['g1_choice']
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()

        pass


class Results(Page):

    def vars_for_template(self):
        return {
            'my_dec': self.player.g1_choice,
            'other_dec': self.player.other_player().g1_choice,
            'same_dec': self.player.other_player().g1_choice==self.player.g1_choice
        }
    pass


page_sequence = [
    Probability,
    Decision,
    ResultsWaitPage,
    Results
]
