"""
Module /rant

Provides the /rant command to the bot.

Classes:
:class RantCollection:
:class RantEntry:
"""

import random
import re


class RantCollection:
    """
    

    Methods:
    :method read_file:
    :method parser_rant:
    :method add_rant:
    :method get_rant_message:
    """

    def __init__(self) -> None:
        self.rant_list = []

    def read_file(self, filename: str) -> None:
        """Read a rant file and add its contents to this collection."""
        with open(filename, "r") as rant_database:
            self.parser_rant(rant_database.readlines())

    def parser_rant(self, raw_data:list[str]) -> None:
        """"""
        # print(raw_data)
        # print("\n\n")
        # print("Einzelrants:")
        # print("\n")

        rant_blocks = []
        
        for start_index in range(len(raw_data)):
            if "<<rant>>" in raw_data[start_index].lower():
                for end_index in range(start_index, len(raw_data)):
                    if "<</rant>>" in raw_data[end_index].lower():
                        rant_blocks.append(raw_data[start_index+1:end_index])
                        # print(f"start_index: {start_index}, end_index: {end_index}")
                        # print(rant_block)
                        # print("\n")
                        break

        # TODO
        # Create lists of start and end indexes (easier to check, maybe more
        # readable).
        
        for rant_data in rant_blocks:
            rant_metadata = dict()
            rant_text = []
            for line in rant_data:
                if re.match(r"\[\[[a-zA-Z0-9]*:.*\]\]", line):
                    key, value = self.get_metadata_from_line(line)
                    rant_metadata[key] = value
                else:
                    rant_text.append(line)
            
            self.add_rant(rant_text, rant_metadata)

        # TODO
        # Make this method resistant to invalid input files.

    def add_rant(self, rant_text, metadata) -> None:
        """Add a single rant entry to the rant collection."""
        new_rant = RantEntry(rant_text, **metadata)
        self.rant_list.append(new_rant)
    
    def get_rant_message(self) -> str:
        """"""
        return(random.choice(self.rant_list).__repr__())

    def get_rant_count(self) -> int:
        """"""
        return len(self.rant_list)
    
    def get_metadata_from_line(self, line:str) -> (str, str):
        """"""
        line_edit = line.lstrip("[").rstrip("\n").rstrip("]")
        line_split = line_edit.split(sep=":",maxsplit=1)
        key = line_split[0].strip().lower()
        value = line_split[1].strip()
        return key, value


class RantEntry:
    """
    

    Methods:
    :method :
    """

    def __init__(self, rant_text_list, date=None, author="Unbekannt"):
        self.date = date
        self.author = author
        # TODO
        # Is there an elegant way to do this?
        rant_text_str = ""
        for line in rant_text_list:
            rant_text_str += line
        self.text = rant_text_str

    def __repr__(self):
        return(f"Rant von {self.author}, gepostet am {self.date}:\n"
               + self.text)
