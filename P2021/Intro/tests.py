from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
import random
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        # ------------------------------------------------------------------------------------------------------------ #
        # submit Intro page
        # ------------------------------------------------------------------------------------------------------------ #
        yield (pages.Intro, {"class_identifier": str(random.choice(list(range(1,5)))) + random.choice(['A','B','C']),
                             "school_identifier": random.choice(["HAK","AHS","MS","Poly"]),
                             "location": random.choice(["school","home"])})
        yield (pages.SubIntro)
