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
    num_rounds = 1
    vac_pay = c(5)
    expl = c(10)
    no_vac = c(2)



class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
    pass


class Group(BaseGroup):


    pass


class Player(BasePlayer):

    prob = models.FloatField(
        verbose_name = 'Please, enter your guess for the probability:',
        max = 100,
        min = 0,

    )

    g1_choice = models.StringField(
        choices=['Cooperate','Defect'],
        widget=widgets.RadioSelect
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):

        payoff_matrix = {
            'Cooperate':
                {
                    'Cooperate': Constants.vac_pay,
                    'Defect': Constants.vac_pay
                },
            'Defect':
                {
                    'Cooperate': Constants.expl,
                    'Defect': Constants.no_vac
                }
        }

        self.payoff = payoff_matrix[self.g1_choice][self.other_player().g1_choice]

    pass
