"""
Stand-alone test module for modules/gp_rant.py
"""

import modules.gp_rant as gp_rant

FILENAME = r"resources/gp_res_rants.txt"

print("Starting rant processing...")
print("Creating RantCollection object...")

RC = gp_rant.RantCollection()

print("Reading rant database...")

RC.read_file(FILENAME)

for rant in RC.rant_list:
    print(rant.__repr__())

print("\n\n")
print(f"Gesamtanzahl gefundener Rants: {RC.get_rant_count()}")