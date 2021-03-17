from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        decoy_valid = {'decoy_t2': random.choice(['C', 'D', 'T'])}
        anchoring_valid = random.choice((
            {"anchoring_t2_buy": 0, 'anchoring_t2_wtp': random.randint(0, 75)},
            {"anchoring_t2_buy": 1, 'anchoring_t2_wtp': random.randint(76, 100)}
        ))
        framing_valid = {'framing_t2': random.choice(['A', 'B'])}
        mental_valid = {'mental_accounting_t2': random.randint(0, 1)}

        page_sequence = {
            'Decoy': {
                1: (pages.Decoy, decoy_valid),
                2: (pages.Anchoring, anchoring_valid),
                3: (pages.Framing, framing_valid),
                4: (pages.MentalAccounting, mental_valid)
            },
            'MentalAccounting': {
                1: (pages.MentalAccounting, mental_valid),
                2: (pages.Framing, framing_valid),
                3: (pages.Anchoring, anchoring_valid),
                4: (pages.Decoy, decoy_valid)
            },
            'Framing': {
                1: (pages.Framing, framing_valid),
                2: (pages.Anchoring, anchoring_valid),
                3: (pages.Decoy, decoy_valid),
                4: (pages.MentalAccounting, mental_valid),
            }
        }

        yield page_sequence[self.participant.vars['task_sequence'][0]][self.round_number]
