from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Claudia Marangon'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'vg_naturalword'
    players_per_group = 2
    num_rounds = 9
    vac_pay = c(5)
    expl = c(10)
    no_vac = c(2)



class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        if self.round_number==1:
            for p in self.get_players():
                p.participant.vars['rand_numb'] = random.randint(1, 9)
                p.participant.vars['rand_game'] = random.randint(1, 2)

    def choice1(self):
        n = 0
        for p in self.get_players():
            if p.g1_choice == 'Choice 1':
                n +=1
        return n

    pass


class Group(BaseGroup):


    pass


class Player(BasePlayer):

    prob = models.FloatField(
        max = 26,
        min = 0,
    )

    g1_choice = models.StringField(
        choices=['Choice 1','Choice 2'],
        widget=widgets.RadioSelect
    )

    elic_pay = models.FloatField()

    def other_player(self):
        return self.get_others_in_group()[0]

    def role(self):
        if self.id_in_group == 1:
            return 'Player A'
        else:
            return 'Player B'

    def set_payoff(self):

        payoff_matrix = {
            'Choice 1':
                {
                    'Choice 1': Constants.vac_pay,
                    'Choice 2': Constants.vac_pay
                },
            'Choice 2':
                {
                    'Choice 1': Constants.expl,
                    'Choice 2': Constants.no_vac
                }
        }

        self.payoff = payoff_matrix[self.g1_choice][self.other_player().g1_choice]

    def display_n(self):
        if self.g1_choice == 'Choice 1' and self.other_player().g1_choice == 'Choice 1':
            n = 2
        elif self.g1_choice == 'Choice 1' or self.other_player().g1_choice == 'Choice 1':
            n = 1
        else:
            n = 0

        return self.subsession.choice1() - n

    def set_payoff_elic(self):

        if self.g1_choice == 'Choice 1' and self.other_player().g1_choice == 'Choice 1':
            n = 2
        elif self.g1_choice == 'Choice 1' or self.other_player().g1_choice == 'Choice 1':
            n = 1
        else:
            n = 0

        if (self.prob - self.subsession.choice1() + n)>0:
            dist = self.prob - self.subsession.choice1() + n
        else:
            dist = self.subsession.choice1() - self.prob - n


        partial_pay = 12 - dist

        if partial_pay >=0:
            self.elic_pay = partial_pay
        else:
            self.elic_pay = 0

    pass
