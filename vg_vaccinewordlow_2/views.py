from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def is_displayed(self):
        return self.round_number==1
    pass

class Disease_details(Page):
    def is_displayed(self):
        return self.round_number==1
pass

class Probability(Page):
    form_model = models.Player
    form_fields = ['prob']
    pass

class Role_alloc(Page):
    def is_displayed(self):
        return self.round_number==1

    def vars_for_template(self):
        return{
            'my_role': self.player.role(),
            'other_role': self.player.other_player().role(),
        }

    pass

class Decision(Page):
    form_model = models.Player
    form_fields = ['g1_choice']
    def vars_for_template(self):
        return{
            'my_role': self.player.role(),
            'round': self.round_number,
        }
    pass

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):

        for p in self.group.get_players():
            if p.round_number==1:
                p.participant.vars['total_p'] = 0
            p.set_payoff()
            p.participant.vars['total_p'] = p.participant.vars['total_p'] + p.payoff

        pass

class ResultsWaitPage2(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        for p in self.subsession.get_players():
            p.set_payoff_elic()

        pass


class Results(Page):

    def before_next_page(self):
        if self.player.round_number == 1:
            self.player.participant.vars['2p_pay'] = 0

        if self.player.round_number == self.player.participant.vars['rand_numb'] and self.player.participant.vars['rand_game'] == 1:
            self.player.participant.vars['2p_pay'] = self.player.payoff
        elif self.player.round_number == self.player.participant.vars['rand_numb'] and self.player.participant.vars['rand_game'] == 2:
            self.player.participant.vars['2p_pay'] = self.player.elic_pay

        if self.player.round_number == 9:
            self.participant.payoff = self.participant.payoff - self.player.participant.vars['total_p'] + self.player.participant.vars['2p_pay']


    def vars_for_template(self):
        return {
            'my_dec': self.player.g1_choice,
            'other_dec': self.player.other_player().g1_choice,
            'same_dec': self.player.other_player().g1_choice==self.player.g1_choice,

        }

    pass

class End(Page):
    def is_displayed(self):
        return self.round_number == 9

    def vars_for_template(self):
        return{
            'rand_r': self.player.participant.vars['rand_numb'],
            'elic': self.player.participant.vars['rand_game'] == 2,
        }

    pass

page_sequence = [
    Instructions,
    Disease_details,
    Role_alloc,
    Decision,
    ResultsWaitPage,
    Probability,
    ResultsWaitPage2,
    Results,
    End
]
