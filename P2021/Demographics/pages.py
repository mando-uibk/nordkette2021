from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models

# ******************************************************************************************************************** #
# *** PAGE DEMOGRAPHIC *** #
# ******************************************************************************************************************** #
class Demographics(Page):

    # specify form field and form model
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    form_fields = ['age','gender','religion','school_type','school_level','math_skill','german_skill',
                   'education_mother','education_father']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):
        # specify info for task progress
        section = 6
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




page_sequence = [Demographics]
