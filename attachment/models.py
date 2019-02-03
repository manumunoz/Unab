from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Manu Munoz Herrera'

doc = """
Attachment Questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'attachment'
    players_per_group = None
    num_rounds = 1
    revkey = 8
    anx_num = 6
    avo_num = 3

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    anxiety = models.IntegerField()
    avoidance = models.IntegerField()

    # def make_field(label):
    #     return models.IntegerField(
    #         choices=[1, 2, 3, 4, 5],
    #         label=label,
    #         widget=widgets.RadioSelect,
    #     )
    #
    # class Player(BasePlayer):
    #     q1 = make_field('I am quick to understand things.')
    #     q2 = make_field('I use difficult words.')
    #     q3 = make_field('I am full of ideas.')
    #     q4 = make_field('I have excellent ideas.')

    attach1 = models.IntegerField(choices=[
            [1, 'Totalmente en desacuerdo'],
            [2, 'En desacuerdo'],
            [3, 'Un poco en desacuerdo'],
            [4, 'Ni de acuerdo ni en desacuerdo'],
            [5, 'Un poco de acuerdo'],
            [6, 'De acuerdo'],
            [7, 'Totalmente de acuerdo'],
    ],
        widget=widgets.RadioSelectHorizontal
    )
    attach2 = models.IntegerField(choices=[
            [1, 'Totalmente en desacuerdo'],
            [2, 'En desacuerdo'],
            [3, 'Un poco en desacuerdo'],
            [4, 'Ni de acuerdo ni en desacuerdo'],
            [5, 'Un poco de acuerdo'],
            [6, 'De acuerdo'],
            [7, 'Totalmente de acuerdo'],
    ],
        # widget=widgets.RadioSelect
    )
    attach3 = models.IntegerField(choices=[
            [1, 'Totalmente en desacuerdo'],
            [2, 'En desacuerdo'],
            [3, 'Un poco en desacuerdo'],
            [4, 'Ni de acuerdo ni en desacuerdo'],
            [5, 'Un poco de acuerdo'],
            [6, 'De acuerdo'],
            [7, 'Totalmente de acuerdo'],
    ],
        # widget=widgets.RadioSelect
    )
    attach4 = models.IntegerField(choices=[
            [1, 'Totalmente en desacuerdo'],
            [2, 'En desacuerdo'],
            [3, 'Un poco en desacuerdo'],
            [4, 'Ni de acuerdo ni en desacuerdo'],
            [5, 'Un poco de acuerdo'],
            [6, 'De acuerdo'],
            [7, 'Totalmente de acuerdo'],
    ],
        # widget=widgets.RadioSelect
    )
    attach5 = models.IntegerField(choices=[
            [1, 'Totalmente en desacuerdo'],
            [2, 'En desacuerdo'],
            [3, 'Un poco en desacuerdo'],
            [4, 'Ni de acuerdo ni en desacuerdo'],
            [5, 'Un poco de acuerdo'],
            [6, 'De acuerdo'],
            [7, 'Totalmente de acuerdo'],
    ],
        # widget=widgets.RadioSelect
    )
    attach6 = models.IntegerField(choices=[
            [1, 'Totalmente en desacuerdo'],
            [2, 'En desacuerdo'],
            [3, 'Un poco en desacuerdo'],
            [4, 'Ni de acuerdo ni en desacuerdo'],
            [5, 'Un poco de acuerdo'],
            [6, 'De acuerdo'],
            [7, 'Totalmente de acuerdo'],
    ],
        # widget=widgets.RadioSelect
    )
    attach7 = models.IntegerField(choices=[
            [1, 'Totalmente en desacuerdo'],
            [2, 'En desacuerdo'],
            [3, 'Un poco en desacuerdo'],
            [4, 'Ni de acuerdo ni en desacuerdo'],
            [5, 'Un poco de acuerdo'],
            [6, 'De acuerdo'],
            [7, 'Totalmente de acuerdo'],
    ],
        # widget=widgets.RadioSelect
    )
    attach8 = models.IntegerField(choices=[
            [1, 'Totalmente en desacuerdo'],
            [2, 'En desacuerdo'],
            [3, 'Un poco en desacuerdo'],
            [4, 'Ni de acuerdo ni en desacuerdo'],
            [5, 'Un poco de acuerdo'],
            [6, 'De acuerdo'],
            [7, 'Totalmente de acuerdo'],
    ],
        # widget=widgets.RadioSelect
    )
    attach9 = models.IntegerField(choices=[
            [1, 'Totalmente en desacuerdo'],
            [2, 'En desacuerdo'],
            [3, 'Un poco en desacuerdo'],
            [4, 'Ni de acuerdo ni en desacuerdo'],
            [5, 'Un poco de acuerdo'],
            [6, 'De acuerdo'],
            [7, 'Totalmente de acuerdo'],
    ],
        # widget=widgets.RadioSelect
    )

    def anx_score(self):
        self.anxiety = ((Constants.revkey-self.attach1)+(Constants.revkey-self.attach2)+(Constants.revkey-self.attach3)+(Constants.revkey-self.attach4)+self.attach5+self.attach6)/Constants.anx_num

    def avo_score(self):
        self.avoidance = (self.attach7+self.attach8+self.attach9)/Constants.avo_num