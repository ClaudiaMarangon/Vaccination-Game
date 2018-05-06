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

class Role_alloc(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'my_role': self.player.role(),
        }

    pass

class Probability(Page):
    form_model = models.Player
    form_fields = ['prob']
    pass

class Decision(Page):
    def is_displayed(self):
        return self.player.role() == 'Player A'
    form_model = models.Group
    form_fields = ['choice_act1']

    def vars_for_template(self):
        return{
            'round': self.round_number,
        }

    pass

class Decision_2(Page):
    def is_displayed(self):
        return self.player.role() == 'Player B'
    form_model = models.Group
    form_fields = ['choice_act2']
    def vars_for_template(self):
        return{
            'round': self.round_number,
        }

    pass

class Decision_p(Page):
    def is_displayed(self):
        return self.player.role() == 'Player C'

    def vars_for_template(self):
        return{
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
    def is_displayed(self):
        return self.player.role() != 'Player C'

    def before_next_page(self):
        if self.player.round_number==1:
            self.player.participant.vars['2p_pay'] = 0

        if self.player.round_number <= 7:
            if self.player.round_number == self.player.participant.vars['rand_numb10'] and self.player.participant.vars['rand_game'] == 1:
                self.player.participant.vars['2p_pay'] = self.player.participant.vars['2p_pay'] + self.player.payoff
            elif self.player.round_number == self.player.participant.vars['rand_numb10'] and self.player.participant.vars['rand_game'] == 2:
                self.player.participant.vars['2p_pay'] = self.player.participant.vars['2p_pay'] + self.player.elic_pay

        if self.player.round_number > 7 and self.player.round_number <= 14:
            if self.player.round_number == self.player.participant.vars['rand_numb20'] and self.player.participant.vars['rand_game'] == 1:
                self.player.participant.vars['2p_pay'] = self.player.participant.vars['2p_pay'] + self.player.payoff
            elif self.player.round_number == self.player.participant.vars['rand_numb20'] and self.player.participant.vars['rand_game'] == 2:
                self.player.participant.vars['2p_pay'] = self.player.participant.vars['2p_pay'] + self.player.elic_pay

        if self.player.round_number > 14 and self.player.round_number <= 21:
            if self.player.round_number == self.player.participant.vars['rand_numb30'] and self.player.participant.vars['rand_game'] == 1:
                self.player.participant.vars['2p_pay'] = self.player.participant.vars['2p_pay'] + self.player.payoff
            elif self.player.round_number == self.player.participant.vars['rand_numb30'] and self.player.participant.vars['rand_game'] == 2:
                self.player.participant.vars['2p_pay'] = self.player.participant.vars['2p_pay'] + self.player.elic_pay

        if self.player.round_number == 21:
            self.participant.payoff = self.participant.payoff - self.player.participant.vars['total_p'] + self.player.participant.vars['2p_pay']


    def vars_for_template(self):
        return {
            'act1': self.player.role()=='Player A',
            'act2': self.player.role()=='Player B',
            'same_dec': self.group.choice_act1==self.group.choice_act2,
            'diff_dec': self.group.choice_act1!=self.group.choice_act2,
            'act1_c': self.group.choice_act1,
            'act2_c': self.group.choice_act2,
        }
    pass

class Results_p(Page):
    def is_displayed(self):
        return self.player.role() == 'Player C'

    def before_next_page(self):
        if self.player.round_number == 1:
            self.player.participant.vars['2p_pay'] = 0

        if self.player.round_number<=7:
            if self.player.round_number == self.player.participant.vars['rand_numb10'] and self.player.participant.vars['rand_game'] == 1:
                self.player.participant.vars['2p_pay'] = self.player.participant.vars['2p_pay'] + self.player.payoff
            elif self.player.round_number == self.player.participant.vars['rand_numb10'] and self.player.participant.vars['rand_game'] == 2:
                self.player.participant.vars['2p_pay'] = self.player.participant.vars['2p_pay'] + self.player.elic_pay

        if self.player.round_number>7 and self.player.round_number<=14:
            if self.player.round_number == self.player.participant.vars['rand_numb20'] and self.player.participant.vars['rand_game'] == 1:
                self.player.participant.vars['2p_pay'] = self.player.participant.vars['2p_pay'] + self.player.payoff
            elif self.player.round_number == self.player.participant.vars['rand_numb20'] and self.player.participant.vars['rand_game'] == 2:
                self.player.participant.vars['2p_pay'] = self.player.participant.vars['2p_pay'] + self.player.elic_pay


        if self.player.round_number>14 and self.player.round_number<=21:
            if self.player.round_number == self.player.participant.vars['rand_numb30'] and self.player.participant.vars['rand_game'] == 1:
                self.player.participant.vars['2p_pay'] = self.player.participant.vars['2p_pay'] + self.player.payoff
            elif self.player.round_number == self.player.participant.vars['rand_numb30'] and self.player.participant.vars['rand_game'] == 2:
                self.player.participant.vars['2p_pay'] = self.player.participant.vars['2p_pay'] + self.player.elic_pay


        if self.player.round_number == 21:
            self.participant.payoff = self.participant.payoff - self.player.participant.vars['total_p'] + self.player.participant.vars['2p_pay']


    def vars_for_template(self):
        return {
            'act1': self.player.role() == 'Player A',
            'act2': self.player.role() == 'Player B',
            'same_dec': self.group.choice_act1 == self.group.choice_act2,
            'diff_dec': self.group.choice_act1 != self.group.choice_act2,
            'act1_c': self.group.choice_act1,
            'act2_c': self.group.choice_act2,
        }
    pass

class End(Page):
    def is_displayed(self):
        return self.round_number == 21

    def vars_for_template(self):
        return{
            'rand_r10': self.player.participant.vars['rand_numb10'],
            'rand_r20': self.player.participant.vars['rand_numb20'],
            'rand_r30': self.player.participant.vars['rand_numb30'],
            'elic': self.player.participant.vars['rand_game'] == 2,
        }
    pass


page_sequence = [
    Instructions,
    Disease_details,
    Role_alloc,
    Decision,
    Decision_2,
    Decision_p,
    ResultsWaitPage,
    Probability,
    ResultsWaitPage2,
    Results,
    Results_p,
    End
]
