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
    code = models.IntegerField(
        verbose_name='Please, enter the last code that you received after the survey:',
    )

    uni_id = models.IntegerField(
        verbose_name='Please, enter your University ID:',
    )

    two_p = models.TextField(
        verbose_name = '[Two-players Game - Max. 150 characters, must not be left blank]',
        max_length = 150
    )

    three_p = models.TextField(
        verbose_name = '[Three-players Game - Max. 150 characters, must not be left blank]',
        max_length = 150
    )

    q1 = models.IntegerField(
        min = 0,
        max = 100,
    )

    q2 = models.IntegerField(
        min = 0,
        max = 100,
    )

    q3 = models.StringField(
        verbose_name = 'Was there anything else you would like to mention regarding the content in the prompt?',
        blank=True
    )

    q4 = models.IntegerField(
        min = 0,
        max = 100,
    )

    q5 = models.StringField(
        verbose_name = 'If in your response to the previous question, you reported that with some probability you may not get vaccinated. Why did you say that?',
        choices=['religious beliefs', 'side effects', 'vaccine will not work', 'good hygiene is enough', 'because most people will already be vaccinated', 'other'],
        blank =True,
    )

    q6 = models.IntegerField(
        min = 0,
        max = 100,
    )

    doc = models.IntegerField(
        verbose_name= 'Doctor/Pediatrician',
        choices=[1, 2, 3, 4, 5, 6]
    )

    par = models.IntegerField(
        verbose_name='Partner/Family',
        choices=[1, 2, 3, 4, 5, 6]
    )

    fre = models.IntegerField(
        verbose_name='Friends',
        choices=[1, 2, 3, 4, 5, 6]
    )

    med = models.IntegerField(
        verbose_name='Internet/Social Media',
        choices=[1, 2, 3, 4, 5, 6]
    )

    tv = models.IntegerField(
        verbose_name='TV/Newspaper/Radio',
        choices=[1, 2, 3, 4, 5, 6]
    )

    oth = models.IntegerField(
        verbose_name='Other',
        choices=[1, 2, 3, 4, 5, 6]
    )

    spec = models.StringField(
        verbose_name='Please specify where you obtain the information you need to make decisions regarding vaccinations.',
    )


    q7 = models.IntegerField(
        min = 0,
        max = 100,
    )

    q8 = models.IntegerField(
        min = 0,
        max = 100,
    )


    pass
