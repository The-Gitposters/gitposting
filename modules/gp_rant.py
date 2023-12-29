"""
Module gp_rant

Provides the following commands to the bot:
    /rant

This module reads rant databases and stores the contents as single rants in
RantEntry objects, which are in turn grouped into RantCollection objects.

TODO:
    Make the RantCollection.parse_rant method resistant to invalid input files.

Classes:
:class RantCollection: Collect and manage RantEntry objects and provide an
    interface to the gitposter bot.
:class RantEntry: Represent single rants and store content and metadata.
"""

import random
import re


class RantCollection:
    """
    Collects and parses rants from one or more rant source files and provides
    methods to manage the rant collection and interface with the gitposter bot.

    Methods:
    :method read_file: 
    :method parse_rant: Parse a rant database block.
    :method get_metadata_from_line: Auxiliary function to split a metadata line
        into a key/value tuple for further processing.
    :method add_rant: Add a new RantEntry object to the internal rant list.
    :method get_rant_message: 
    :method get_rant_count: 

    Class variables:
    :variable rant_list: Contains rants as RantEntry objects.
    """

    def __init__(self) -> None:
        """Initialise the RantCollection object with an empty rant list."""
        self.rant_list = []

    def read_file(self, filename:str) -> None:
        """
        Read a rant file and add pass the content to the parser_rant method, as
        array of lines.
        """
        with open(filename, "r", encoding="utf-8") as rant_database:
            self.parse_rant(rant_database.readlines())

    def parse_rant(self, raw_data:list[str]) -> None:
        """
        Parse a raw text block from a rant database file and add the contents
        to this RantCollection's rant list.
        """
        start_index_list = []
        end_index_list = []

        # Search lines that contain the phrases "<<rant>>" as key sequence to
        # start a rant and "<</rant>>" as key sequence to conclude a rant.
        # Collect indices of these lines that start and end rants.
        for index in range(len(raw_data)):
            if "<<rant>>" in raw_data[index].lower():
                start_index_list.append(index)
            if "<</rant>>" in raw_data[index].lower():
                end_index_list.append(index)
        
        # Process every block of lines between a <<rant>> and a <</rant>>
        for start_index in start_index_list:
            end_index = end_index_list.pop(0) - 1
            # Initialise rant data as empty metadata dictionary and empty string
            # for the actual rant text.
            rant_metadata = dict()
            rant_text = ""
            for line in raw_data[start_index:end_index]:
                # Metadata lines have the following structure:
                # [[<variable-name>: <value>]]
                if re.match(r"\[\[[a-zA-Z0-9]*:.*\]\]", line):
                    key, value = self.get_metadata_from_line(line)
                    rant_metadata[key] = value
                # Every other line is considered to contain rant text.
                else:
                    rant_text += line
            
            # Add rant to the collection
            self.add_rant(rant_text, rant_metadata)

        # TODO
        # Make this method resistant to invalid input files.
    
    def get_metadata_from_line(self, line:str) -> (str, str):
        """Extract a key/value pair from a metadata line in the database."""
        line_edit = line.lstrip("[").rstrip("\n").rstrip("]")
        line_split = line_edit.split(sep=":",maxsplit=1)
        key = line_split[0].strip().lower()
        value = line_split[1].strip()
        return key, value

    def add_rant(self, rant_text:str, metadata:dict) -> None:
        """Add a single rant entry to the rant collection."""
        new_rant = RantEntry(rant_text, **metadata)
        self.rant_list.append(new_rant)
    
    def get_rant_message(self) -> str:
        """Return a random rant message."""
        return(random.choice(self.rant_list).__repr__())

    def get_rant_count(self) -> int:
        """Return the length of the internal rant list."""
        return len(self.rant_list)


class RantEntry:
    """
    Represents a single rant and manages its text as well as metadata.

    Methods:
    :method __repr__: Return a string representation of the rant. Can be
        modified to change the format.

    Class variables:
    :variable text: Contains the entire rant text, including line breaks.

    Rant metadata:
    Metadata are to be included in the rant source file in one line per variable
    which has to be the following form:
    [[<variable-name>: <value>]]
        (double brackets [[ and ]] are to be interpreted as literals.)
    :date: Date of the original post that contained the rant
    :author: Original rant author.
    """

    def __init__(self, rant_text:str, date:str=None, author:str="Unbekannt"):
        self.date = date
        self.author = author
        self.text = rant_text

    def __repr__(self) -> str:
        """Return a string representation of the rant."""
        return(f"Rant von {self.author}, gepostet am {self.date}:\n"
               + self.text)
