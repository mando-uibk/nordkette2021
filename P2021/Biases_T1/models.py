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
Treatment 1 for biases Decoy, Anchoring, Framing, Mental Accounting and Conjunction Fallacy
"""


# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class Constants(BaseConstants):
    name_in_url = 'Biases_T1'
    players_per_group = None
    task_sequences = [
        ['Decoy', 'Anchoring', 'Framing', 'MentalAccounting'],
        ['MentalAccounting', 'Framing', 'Anchoring', 'Decoy'],
        ['Framing', 'Anchoring', 'Decoy', 'MentalAccounting']
    ]
    num_rounds = 5  # length of task_sequences + 1 for Conjunction Fallacy


# ******************************************************************************************************************** #
# *** CLASS SUBSESSION *** #
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                round_numbers = list(range(1, Constants.num_rounds+1))
                task_sequence = random.choice(Constants.task_sequences) + ['ConjunctionFallacy']
                p.participant.vars["page_count"] = 1
                p.participant.vars["page_sequence"] = dict(zip(task_sequence, round_numbers))
                p.participant.vars["task_sequence"] = task_sequence
                p.page_sequence_t1 = json.dumps(task_sequence)



# ******************************************************************************************************************** #
# *** CLASS GROUP *** #
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass

# ******************************************************************************************************************** #
# *** CLASS PLAYER *** #
# ******************************************************************************************************************** #
class Player(BasePlayer):
    page_sequence_t1 = models.StringField()
    decoy_t1 = models.StringField()
    anchoring_t1_wtp = models.FloatField()
    framing_t1 = models.StringField()
    mental_accounting_t1 = models.IntegerField()
    conjunction_fallacy = models.IntegerField()



