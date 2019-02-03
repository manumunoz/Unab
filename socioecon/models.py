from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Manu Munoz Herrera'

doc = """
Socioeconomic Questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'socioecon'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    estrato = models.IntegerField(choices=[
            [1, 'Estrato 1'],
            [2, 'Estrato 2'],
            [3, 'Estrato 3'],
            [4, 'Estrato 4'],
            [5, 'Estrato 5'],
            [6, 'Estrato 6'],
        ],
        # widget=widgets.RadioSelect
    )
    edupadre = models.IntegerField(choices=[
            [1, 'Primaria'],
            [2, 'Bachillerato'],
            [3, 'Universidad'],
            [4, 'Especialización'],
            [5, 'Maestría'],
            [6, 'Doctorado'],
            [7, 'No sabe / no aplica'],
    ],
        # widget=widgets.RadioSelect
    )
    edumadre = models.IntegerField(choices=[
            [1, 'Primaria'],
            [2, 'Bachillerato'],
            [3, 'Universidad'],
            [4, 'Especialización'],
            [5, 'Maestría'],
            [6, 'Doctorado'],
            [7, 'No sabe / no aplica'],
    ],
        # widget=widgets.RadioSelect
    )
    colegio = models.IntegerField(choices=[
            [1, 'Semestralizado'],
            [2, 'Validación'],
            [3, 'Público'],
            [4, 'Privado'],
            [5, 'Otro'],
        ],
        # widget=widgets.RadioSelect
    )
    ingresos = models.IntegerField(choices=[
            [1, 'Mayores que los de las familias de sus compañeros'],
            [2, 'Iguales a los de las familias de sus compañeros'],
            [3, 'Menores  que los de las familias de sus compañeros'],
        ],
        # widget=widgets.RadioSelect
    )
    piel = models.IntegerField(choices=[
            [1, 'Muchas veces'],
            [2, 'Algunas veces'],
            [3, 'Pocas veces'],
            [4, 'Nunca'],
        ],
        # widget=widgets.RadioSelect
    )
    genero = models.IntegerField(choices=[
            [1, 'Muchas veces'],
            [2, 'Algunas veces'],
            [3, 'Pocas veces'],
            [4, 'Nunca'],
        ],
        # widget=widgets.RadioSelect
    )
    condicion = models.IntegerField(choices=[
            [1, 'Muchas veces'],
            [2, 'Algunas veces'],
            [3, 'Pocas veces'],
            [4, 'Nunca'],
        ],
        # widget=widgets.RadioSelect
    )

    posturahoy = models.IntegerField(choices=[1,2,3,4,5,6,7,8,9,10],
                                     # widget=widgets.RadioSelect
    )
    posturapasado = models.IntegerField(choices=[
            [1, 'Más a la izquierda'],
            [2, 'Igual'],
            [3, 'Más a la derecha'],
        ],
        # widget=widgets.RadioSelect
    )
    posturafuturo = models.IntegerField(choices=[
            [1, 'Más a la izquierda'],
            [2, 'Igual'],
            [3, 'Más a la derecha'],
        ],
        # widget=widgets.RadioSelect
    )

