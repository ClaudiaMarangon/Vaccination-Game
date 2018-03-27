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
    name_in_url = 'vg_naturalword_3'
    players_per_group = 3
    num_rounds = 1
    vac_pay = c(5)
    expl = c(8)
    no_vac = c(2)
    no_vac_pp = c(0)
    vac_novac = c(4)



class Subsession(BaseSubsession):
    def creating_session(self):


        self.group_randomly()

        for g in self.get_groups():
            pl_list = (1, 2, 3)
            g.pass_p1 = random.choice(pl_list)
            g.act1 = g.pass_p1
            while g.act1==g.pass_p1:
                g.act1 = random.choice(pl_list)
    pass


class Group(BaseGroup):

    pass_p1 = models.IntegerField()
    act1 = models.IntegerField()

    choice_act1 = models.StringField(
        choices=['Cooperate','Defect'],
        widget=widgets.RadioSelect
    )

    choice_act2 = models.StringField(
        choices=['Cooperate','Defect'],
        widget=widgets.RadioSelect
    )

    pass


class Player(BasePlayer):

    prob = models.FloatField(
        max = 22,
        min = 0,
    )

    def role(self):
        if self.id_in_group == self.group.pass_p1:
            return 'Passive'
        elif self.id_in_group == self.group.act1:
            return 'Active1'
        else:
            return 'Active2'

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff_matrix_act = {
            'Cooperate':
                {
                    'Cooperate': Constants.vac_pay,
                    'Defect': Constants.vac_novac
                },
            'Defect':
                {
                    'Cooperate': Constants.expl,
                    'Defect': Constants.no_vac
                }
        }

        payoff_matrix_pass = {
            'Cooperate':
                {
                    'Cooperate': Constants.vac_pay,
                    'Defect': Constants.vac_novac
                },
            'Defect':
                {
                    'Cooperate': Constants.vac_novac,
                    'Defect': Constants.no_vac_pp
                }
        }

        if self.role()=='Active1':
            self.payoff = payoff_matrix_act[self.group.choice_act1][self.group.choice_act2]
        elif self.role()=='Active2':
            self.payoff = payoff_matrix_act[self.group.choice_act2][self.group.choice_act1]
        else:
            self.payoff = payoff_matrix_pass[self.group.choice_act1][self.group.choice_act2]


    pass