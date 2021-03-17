from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random
import itertools
import json


author = 'Armando Holzknecht'

doc = """
Treatment 2 for biases Decoy, Anchoring, Framing, Mental Accounting and Conjunction Fallacy
"""

# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class Constants(BaseConstants):
    name_in_url = 'Biases_T2'
    players_per_group = None
    num_rounds = 4  # one less than in T1, Conjunction Fallacy is missing.

# ******************************************************************************************************************** #
# *** CLASS SUBSESSION *** #
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                round_numbers = list(range(1, Constants.num_rounds+1))
                task_sequence = p.participant.vars["task_sequence"][:-1]  # without Conjunction Fallacy
                p.participant.vars["page_sequence"] = dict(zip(task_sequence, round_numbers))
                p.page_sequence_t2 = json.dumps(task_sequence)

# ******************************************************************************************************************** #
# *** CLASS GROUP *** #
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass

# ******************************************************************************************************************** #
# *** CLASS PLAYER *** #
# ******************************************************************************************************************** #
class Player(BasePlayer):
    page_sequence_t2 = models.StringField()
    decoy_t2 = models.StringField()
    anchoring_t2_wtp = models.FloatField()
    anchoring_t2_buy = models.IntegerField()
    framing_t2 = models.StringField()
    mental_accounting_t2 = models.IntegerField()
