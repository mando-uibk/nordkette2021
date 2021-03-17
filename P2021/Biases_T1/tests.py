from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
import random
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        decoy_valid = {'decoy_t1': random.choice(['C', 'T'])}
        anchoring_valid = {'anchoring_t1_wtp': random.randint(0, 100)}
        framing_valid = {'framing_t1': random.choice(['A', 'B'])}
        mental_valid = {'mental_accounting_t1': random.randint(0, 1)}
        conjunction_valid = {'conjunction_fallacy': random.randint(0,1)}

        page_sequence = {
            'Decoy': {
                1: (pages.Decoy, decoy_valid),
                2: (pages.Anchoring, anchoring_valid),
                3: (pages.Framing, framing_valid),
                4: (pages.MentalAccounting, mental_valid),
                5: (pages.ConjunctionFallacy, conjunction_valid)
            },
            'MentalAccounting': {
                1: (pages.MentalAccounting, mental_valid),
                2: (pages.Framing, framing_valid),
                3: (pages.Anchoring, anchoring_valid),
                4: (pages.Decoy, decoy_valid),
                5: (pages.ConjunctionFallacy, conjunction_valid)
            },
            'Framing': {
                1: (pages.Framing, framing_valid),
                2: (pages.Anchoring, anchoring_valid),
                3: (pages.Decoy, decoy_valid),
                4: (pages.MentalAccounting, mental_valid),
                5: (pages.ConjunctionFallacy, conjunction_valid)
            }
        }

        yield page_sequence[self.participant.vars['task_sequence'][0]][self.round_number]
