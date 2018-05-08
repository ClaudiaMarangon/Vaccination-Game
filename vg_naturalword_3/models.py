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
    num_rounds = 21
    vac_pay = c(5)
    expl = c(10)
    no_vac = c(2)
    no_vac_pp = c(0)
    vac_novac = c(5)
    vac_novac_pp = c(2)



class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)

        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['rand_numb10'] = random.randint(1, 7)
                p.participant.vars['rand_numb20'] = random.randint(8, 14)
                p.participant.vars['rand_numb30'] = random.randint(15, 21)
                p.participant.vars['rand_game'] = random.randint(1, 2)

        for g in self.get_groups():
            if self.round_number<=7: #for the first 10 rounds P2 is Player C and P3 is Player A
                g.pass_p1 = 2
                g.act1 = 3
            elif self.round_number>7 and self.round_number<=14: #for the second 10 rounds P3 is Player C and P1 is Player A
                g.pass_p1 = 3
                g.act1 = 1
            elif self.round_number>14: #for the last 10 rounds P1 is Player C and P2 is Player A
                g.pass_p1 = 1
                g.act1 = 2

    def choice1(self):
        n = 0
        for g in self.get_groups():
            if g.choice_act1 == 'Choice 1' and g.choice_act2 == 'Choice 1':
                n +=2
            elif g.choice_act1 == 'Choice 1' or g.choice_act2 == 'Choice 1':
                n += 1
        return n

    pass


class Group(BaseGroup):

    pass_p1 = models.IntegerField()
    act1 = models.IntegerField()

    choice_act1 = models.StringField(
        choices=['Choice 1','Choice 2'],
        widget=widgets.RadioSelect
    )

    choice_act2 = models.StringField(
        choices=['Choice 1','Choice 2'],
        widget=widgets.RadioSelect
    )

    pass


class Player(BasePlayer):

    prob = models.FloatField(
        max = 22,
        min = 0,
    )

    elic_pay = models.FloatField()

    def role(self):
        if self.id_in_group == self.group.pass_p1:
            return 'Player C'
        elif self.id_in_group == self.group.act1:
            return 'Player A'
        else:
            return 'Player B'

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff_matrix_act = {
            'Choice 1':
                {
                    'Choice 1': Constants.vac_pay,
                    'Choice 2': Constants.vac_novac
                },
            'Choice 2':
                {
                    'Choice 1': Constants.expl,
                    'Choice 2': Constants.no_vac
                }
        }

        payoff_matrix_pass = {
            'Choice 1':
                {
                    'Choice 1': Constants.vac_pay,
                    'Choice 2': Constants.vac_novac_pp
                },
            'Choice 2':
                {
                    'Choice 1': Constants.vac_novac_pp,
                    'Choice 2': Constants.no_vac_pp
                }
        }

        if self.role()=='Player A':
            self.payoff = payoff_matrix_act[self.group.choice_act1][self.group.choice_act2]
        elif self.role()=='Player B':
            self.payoff = payoff_matrix_act[self.group.choice_act2][self.group.choice_act1]
        else:
            self.payoff = payoff_matrix_pass[self.group.choice_act1][self.group.choice_act2]

    def set_payoff_elic(self):

        if self.group.choice_act1 == 'Choice 1' and self.group.choice_act2 == 'Choice 1':
            n = 2
        elif self.group.choice_act1 == 'Choice 1' or self.group.choice_act2 == 'Choice 1':
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

    def display_n(self):
        if self.group.choice_act1 == 'Choice 1' and self.group.choice_act2 == 'Choice 1':
            n = 2
        elif self.group.choice_act1 == 'Choice 1' or self.group.choice_act2 == 'Choice 1':
            n = 1
        else:
            n = 0

        return self.subsession.choice1() - n

    pass