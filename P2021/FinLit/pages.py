from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models

# ******************************************************************************************************************** #
# *** PAGE SUB INTRO *** #
# ******************************************************************************************************************** #
class SubIntro(Page):
    # time out
    # ----------------------------------------------------------------------------------------------------------------
    timeout_seconds = 30
    timer_text = "Verbleibende Zeit bis du automatisch weitergeleitet wirst:"

# ******************************************************************************************************************** #
# *** PAGE FINLIT *** #
# ******************************************************************************************************************** #
class FinLit(Page):

    #specify form models and form fields
    form_model = 'player'
    form_fields = ['interest_compounding','real_interest','diversification',
                   'bond_pricing','credit_interest']

    def vars_for_template(self):
        # specify info for task progress
        section = 2
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 1
        page = self.subsession.round_number
        progress = page / total * 100

        return {
            'section': section,
            'section_total': section_total,
            'section_progress': section_progress,
            'page': page,
            'total': total,
            'progress': progress,
        }

page_sequence = [SubIntro, FinLit]
