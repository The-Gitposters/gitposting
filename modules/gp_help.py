"""
provides a manual-message when "/help" ist called
the user can pass the names of commands, he/she wants to receive more information on

"""

# define constant used variables
# resource_file_separator is used to split the commands in the help text file.
# it is being filtered out in the output and should be very unlikely to be used in plain text.
resource_file_separator = "&&%&"

def babysit_these_morons(message):
    # load resource
    helptext = open('resources/gp_res_help.txt', encoding='utf-8').read()
    
    # check for arguments passed after the /help command. message is split by blank spaces
    number_of_arguments = len(str(message.text).split(' '))

    # no argument was passed, print whole help-page
    if(number_of_arguments <= 1):
        return helptext.replace(resource_file_separator, '')
    else:
        # DEBUG
        # separating passed arguments into an array
        arguments = str(message.text).split(' ')[1:]
        # separating helptext entrys and stripping the / 
        helptext_lines = helptext.split(resource_file_separator + "/")
        # declaring string to return
        return_helptext = ""
        # iterate through the helptext lines and check which commands are asked for
        for helptext_line in helptext_lines:
            # iterate through asked commands
            for argument in arguments:
                # check if argument is a command that's noted in helptext
                if str(helptext_line)[:len(argument) + 1] == argument + "\n":
                    # add command help entry
                    return_helptext += "/" + helptext_line
        return return_helptext