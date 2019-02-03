from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Attach_Quest(Page):
    form_model = 'player'
    form_fields = ['attach1','attach2','attach3','attach4','attach5','attach6','attach7','attach8', 'attach9']

    def before_next_page(self):
        self.player.anx_score()
        self.player.avo_score()


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass
#
#
# class Results(Page):
#     pass


page_sequence = [
    Attach_Quest,
    ResultsWaitPage,
    # Results
]
