from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'vg_vaccineword'
    players_per_group = 2
    num_rounds = 1
    vac_pay = c(5)
    expl = c(10)
    no_vac = c(2)



class Subsession(BaseSubsession):
#    def creating_session(self):
 #       self.group_randomly()
#
 #       for g in self.get_groups():
  #          pl_list = (1, 2, 3, 4, 5, 6)
   #         g.pass_p1 = random.choice(pl_list)
    #        pl_list.remove(g.pass_p1)
     #       g.pass_p2 = random.choice(pl_list)
    pass


class Group(BaseGroup):

    #pass_p1 = models.IntegerField()
    #pass_p2 = models.IntegerField()


    pass


class Player(BasePlayer):

    #def role(self):
     #   if self.id_in_group == Group.pass_p1 or self.id_in_group == Group.pass_p2:
      #      return 'Passive'
       # else:
        #    return 'Active'

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