"""
Module

Methods:
:method get_peptalk: Returns a randomised pep talk sequence.
"""

import random

# Entries for the pep talk generator
# A pep talk response consists of four parts, each taken from one of the lists
# below, in the order of INTRO, SUBJECT, ACTION, CLOSING.
LIST_PEP_INTRO = [
    "Champ,",
    "Fact:",
    "Everybody says",
    "Dang...",
    "Check it:",
    "Just saying...",
    "Superstar,",
    "Tiger,",
    "Self,",
    "Know this:",
    "News alert:",
    "Scientists baffled:",
    "Ace,",
    "Excuse me but",
    "Experts agree:",
    "In my opinion",
    "Hear ye, hear ye:",
    "Okay, listen up:"
]

LIST_PEP_SUBJECT = [
    "the mere idea of you",
    "your soul",
    "your hair today",
    "everything you do",
    "your personal style",
    "every thought you have",
    "that sparkle in your eye",
    "your presence here",
    "what you got going on",
    "the essential you",
    "your life's journey",
    "that saucy personality",
    "your DNA",
    "the brain of yours",
    "your choice of attire",
    "the way you roll",
    "whatever your secret is",
    "all of y'all"
]

LIST_PEP_ACTION = [
    "has serious game",
    "rains magic",
    "deserfves the Nobel Prize",
    "raises the roof",
    "breeds miracles",
    "is paying off big time",
    "shows mad skills",
    "just shimmers",
    "is a national treasure",
    "gets the party hopping",
    "is the next big thing",
    "roars like a lion",
    "is a rainbow factory",
    "is made of diamonds",
    "makes birds sing",
    "should be taught in school",
    "makes my world go 'round",
    "is 100%% legit"
]

LIST_PEP_CLOSING = [
    "24/7.",
    "can I get an amen?",
    "and that's a fact.",
    "so treat yourself.",
    "you feel me?",
    "that's just science.",
    "would I lie?",
    "for reals.",
    "mic drop.",
    "you hidden gem.",
    "snuggle bear.",
    "period.",
    "yo.",
    "now let's dance",
    "high five.",
    "say it again!",
    "according to CNN.",
    "so get used to it."
]


def get_peptalk():
    """Return a randomised pep talk as a single string."""
    return(
        random.choice(LIST_PEP_INTRO)
        + " "
        + random.choice(LIST_PEP_SUBJECT)
        + " "
        + random.choice(LIST_PEP_ACTION)
        + ", "
        + random.choice(LIST_PEP_CLOSING)
    )

# Initialise random number generator with system time on module import.
random.seed(a=None)