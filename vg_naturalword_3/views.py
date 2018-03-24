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

class Decision(Page):
    def is_displayed(self):
        return self.player.role() == 'Active1'
    form_model = models.Group
    form_fields = ['choice_act1']
    pass

class Decision_2(Page):
    def is_displayed(self):
        return self.player.role() == 'Active2'
    form_model = models.Group
    form_fields = ['choice_act2']
    pass

class Decision_p(Page):
    def is_displayed(self):
        return self.player.role() == 'Passive'

    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()
        pass


class Results(Page):
    def is_displayed(self):
        return self.player.role() != 'Passive'

    def vars_for_template(self):
        return {
            'act1': self.player.role()=='Active1',
            'act2': self.player.role()=='Active2',
            'same_dec': self.group.choice_act1==self.group.choice_act2,
            'diff_dec': self.group.choice_act1!=self.group.choice_act2,
            'act1_c': self.group.choice_act1,
            'act2_c': self.group.choice_act2,
        }
    pass

class Results_p(Page):
    def is_displayed(self):
        return self.player.role() == 'Passive'

    def vars_for_template(self):
        return {
            'act1': self.player.role() == 'Active1',
            'act2': self.player.role() == 'Active2',
            'same_dec': self.group.choice_act1 == self.group.choice_act2,
            'diff_dec': self.group.choice_act1 != self.group.choice_act2,
            'act1_c': self.group.choice_act1,
            'act2_c': self.group.choice_act2,
        }
    pass


page_sequence = [
    Probability,
    Decision,
    Decision_2,
    Decision_p,
    ResultsWaitPage,
    Results,
    Results_p
]
