from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import json

# ******************************************************************************************************************** #
# *** PAGE DECOY *** #
# ******************************************************************************************************************** #
class Decoy(Page):
    def is_displayed(self):
        return self.round_number == self.participant.vars['page_sequence']['Decoy']

    def before_next_page(self):
        self.participant.vars["page_count"] += 1
        if self.round_number != 1:
            self.player.in_round(1).decoy_t2 = self.player.decoy_t2

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['decoy_t2']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for task progress
        section = 5
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 4
        page = self.participant.vars["page_count"]
        progress = page / total * 100

        return {
            'section':          section,
            'section_total':    section_total,
            'section_progress': section_progress,
            'page':          page,
            'total':         total,
            'progress':      progress,
        }


# ******************************************************************************************************************** #
# *** PAGE ANCHORING *** #
# ******************************************************************************************************************** #
class Anchoring(Page):
    def is_displayed(self):
        return self.round_number == self.participant.vars['page_sequence']['Anchoring']

    def before_next_page(self):
        self.participant.vars["page_count"] += 1
        if self.round_number != 1:
            self.player.in_round(1).anchoring_t2_buy = self.player.anchoring_t2_buy
            self.player.in_round(1).anchoring_t2_wtp = self.player.anchoring_t2_wtp

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['anchoring_t2_buy','anchoring_t2_wtp']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for task progress
        section = 5
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 4
        page = self.participant.vars["page_count"]
        progress = page / total * 100

        return {
            'section':          section,
            'section_total':    section_total,
            'section_progress': section_progress,
            'page':          page,
            'total':         total,
            'progress':      progress,
        }



# ******************************************************************************************************************** #
# *** PAGE FRAMING *** #
# ******************************************************************************************************************** #
class Framing(Page):
    def is_displayed(self):
        return self.round_number == self.participant.vars['page_sequence']['Framing']

    def before_next_page(self):
        self.participant.vars["page_count"] += 1
        if self.round_number != 1:
            self.player.in_round(1).framing_t2 = self.player.framing_t2

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['framing_t2']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for task progress
        section = 5
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 4
        page = self.participant.vars["page_count"]
        progress = page / total * 100

        return {
            'section':          section,
            'section_total':    section_total,
            'section_progress': section_progress,
            'page':          page,
            'total':         total,
            'progress':      progress,
        }

# ******************************************************************************************************************** #
# *** PAGE MENTAL ACCOUNTING *** #
# ******************************************************************************************************************** #
class MentalAccounting(Page):
    def is_displayed(self):
        return self.round_number == self.participant.vars['page_sequence']['MentalAccounting']

    def before_next_page(self):
        self.participant.vars["page_count"] += 1
        if self.round_number != 1:
            self.player.in_round(1).mental_accounting_t2 = self.player.mental_accounting_t2

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['mental_accounting_t2']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for task progress
        section = 5
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 4
        page = self.participant.vars["page_count"]
        progress = page / total * 100

        return {
            'section':          section,
            'section_total':    section_total,
            'section_progress': section_progress,
            'page':          page,
            'total':         total,
            'progress':      progress,
        }


page_sequence = [
    Decoy,
    Anchoring,
    Framing,
    MentalAccounting,
]