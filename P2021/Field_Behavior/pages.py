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
# *** PAGE RISK PREFERENCE *** #
# ******************************************************************************************************************** #
class Field_Behavior(Page):
    #specify form models and form fields
    form_model = 'player'
    form_fields = ['gambling','general_risk','saving','temptation']

    def vars_for_template(self):
        # specify info for task progress
        section = 4
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 2
        page = 1
        progress = page / total * 100

        return {
            'section': section,
            'section_total': section_total,
            'section_progress': section_progress,
            'page': page,
            'total': total,
            'progress': progress,
        }

class Perception_Questions(Page):
    #specify form models and form fields
    form_model = 'player'
    form_fields = ['financial_troubles','fin_education_school','fin_education_parents']

    def vars_for_template(self):
        # specify info for task progress
        section = 4
        section_total = 6
        section_progress = section / section_total * 100

        # specify info for progress bar
        total = 2
        page = 2
        progress = page / total * 100

        return {
            'section': section,
            'section_total': section_total,
            'section_progress': section_progress,
            'page': page,
            'total': total,
            'progress': progress,
        }

# ******************************************************************************************************************** #
# *** PAGE SUB INTRO BIASES T2*** #
# ******************************************************************************************************************** #
class SubIntroB2(Page):
    # time out
    # ----------------------------------------------------------------------------------------------------------------
    timeout_seconds = 30
    timer_text = "Verbleibende Zeit bis du automatisch weitergeleitet wirst:"

page_sequence = [SubIntro, Field_Behavior, Perception_Questions, SubIntroB2]
