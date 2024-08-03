__doc__ = "This is a Code snippet for Parsing through a nested dictionary and searching for values from an another list " \
          "This was used in Pyrevit Code snippet ConColSchedulerXLView"
__author__ = 'Abhishek Shinde | Silman Colab'
__contact__ = 'abhishek.shinde@silman.com | arabhishek1091@gmail.com'
__copyright__ = 'SILMAN COLAB- Silman Structural Solutions'

"""
Problem Statement
******************

We have a nested dictionary "CCSXLMarks" which has the name of the Marks of Concrete Columns designated as "Cx".
x is a placeholder of column number. This top level key "Cx" stores a list of Column Attributes as a second dictionary.
The Column Attributes are "BL" which means Base Level. "SFN" is a proprietary term of Silman  and "TL" means Top Level.

Here we are reading the nested dictionary and searching if attribute "BL" or "TL" has the data of the levels included
inside the list "Levels_to_search_for"
Then for every item of the Levels list we print its value.

"""

# Function to process Levels based on concreteColumnMarks Dictionary
def process_levels(levelstosearchfor, concretecolumnmarksDict):
    result = {level: [] for level in levelstosearchfor}

    for key, values in concretecolumnmarksDict.items():
        for value in values:
            b1_level = int(value["BL"].split()[-1])
            t1_level = int(value["TL"].split()[-1])

            for level in range(b1_level, t1_level + 1):
                result[f"Level {level}"].append(value["SFN"])

    return result

# Problem Statement - NOTE THIS DATA IS A PLACEHOLDER SILMAN'S DATA AND DOES NOT HOLD ANY PROJECT'S DATA OF SILMAN
Levels_to_search_for = ['Level 5', 'Level 4', 'Level 3', 'Level 2', 'Level 1', 'Survey']
# CCSLMarks means Concrete Column Excel Marks
CCSXLMarks = {'C2': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '14x14 (8)#11', 'TL': 'Level 4'}],
              'C9': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '14x14 (8)#11', 'TL': 'Level 4'}],
              'C5': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '14x14 (8)#11', 'TL': 'Level 4'}],
              'C8': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '14x14 (8)#11', 'TL': 'Level 4'}],
              'C16': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '14x14 (8)#11', 'TL': 'Level 4'}],
              'C3': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '14x14 (8)#11', 'TL': 'Level 4'}],
              'C14': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '14x14 (8)#11', 'TL': 'Level 4'}],
              'C15': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '14x14 (8)#11', 'TL': 'Level 4'}],
              'C12': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '14x14 (8)#11', 'TL': 'Level 4'}],
              'C13': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '14x14 (8)#11', 'TL': 'Level 4'}],
              'C10': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '18x18 (12)#10', 'TL': 'Level 4'}],
              'C11': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '18x18 (12)#10', 'TL': 'Level 4'}],
              'C1': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '14x14 (8)#11', 'TL': 'Level 4'}],
              'C6': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '18x18 (12)#10', 'TL': 'Level 4'}],
              'C4': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '14x14 (8)#11', 'TL': 'Level 4'}],
              'C7': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '18x18 (12)#10', 'TL': 'Level 4'}]}

# Final Output for Processing Level and Marks information
final_output = process_levels(Levels_to_search_for, CCSXLMarks)

# Print the final output
print("Final Output after Level Processing:")
for level, values in final_output.items():
    print(f"{level} = {values}")

# Add debugging prints
print("Debugging Prints:")
for key, value in CCSXLMarks.items():
    print(f"Processing {key}:")
    b1_level = int(value[0]["BL"].split()[-1])
    t1_level = int(value[0]["TL"].split()[-1])
    print(f"  b1_level: {b1_level}, t1_level: {t1_level}")
    for level in range(b1_level, t1_level + 1):
        sfn_values = [item['SFN'] for item in value]
        print(f"  Level {level} = {sfn_values}")
