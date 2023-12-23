"""
CAPSPAM-Module.
Capspam is used to send one message per character in certain words which are written in CAPS by another group user

Example:
Maggsime types "... CLIGGE..."
Bot responds
"C"
"L"
"I"
"G"
"G"
"E"

"""

capspam_triggers = [
    "CLIGGE",
    "EGG",
    "CHEESE"
]

def get_capspam_result(message):
    """ Searches for capspam triggerword (defined in capspam_triggers) """
    for capspam_trigger in capspam_triggers:
        if(str(message).__contains__(capspam_trigger)):
            return capspam_trigger
    return ""
