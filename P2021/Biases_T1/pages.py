from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import random
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
            self.player.in_round(1).decoy_t1 = self.player.decoy_t1

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    form_fields = ['decoy_t1']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for task progress
        section = 1
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 5
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
            self.player.in_round(1).anchoring_t1_wtp = self.player.anchoring_t1_wtp

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    form_fields = ['anchoring_t1_wtp']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):
        # specify info for task progress
        section = 1
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 5
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
            self.player.in_round(1).framing_t1 = self.player.framing_t1

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    form_fields = ['framing_t1']


    def vars_for_template(self):
        # specify info for task progress
        section = 1
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 5
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
            self.player.in_round(1).mental_accounting_t1 = self.player.mental_accounting_t1

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    form_fields = ['mental_accounting_t1']

    def vars_for_template(self):
        # specify info for task progress
        section = 1
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 5
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
# *** PAGE CONJUNCTION FALLACY *** #
# ******************************************************************************************************************** #
class ConjunctionFallacy(Page):
    def is_displayed(self):
        return self.round_number == 5  # always shown last

    def before_next_page(self):
        self.participant.vars["page_count"] = 1
        if self.round_number != 1:
            self.player.in_round(1).conjunction_fallacy = self.player.conjunction_fallacy

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    form_fields = ['conjunction_fallacy']

    def vars_for_template(self):
        # specify info for task progress
        section = 1
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 5
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
    ConjunctionFallacy
]
