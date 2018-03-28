from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    two_p = models.TextField(
        verbose_name = '[Two-players Game - Max. 150 characters, must not be left blank]',
        max_length = 150
    )

    three_p = models.TextField(
        verbose_name = '[Three-players Game - Max. 150 characters, must not be left blank]',
        max_length = 150
    )

    pass
