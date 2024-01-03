__doc__ = "This is a Code snippet for sorting a nested dictionary by the numerical sorting of the second character of the primary key(outside)" \
          "This was used in Pyrevit Code snippet ConColSchedulerXLView"
__author__ = 'Abhishek Shinde | Silman Colab'
__contact__ = 'abhishek.shinde@silman.com | arabhishek1091@gmail.com'
__copyright__ = 'SILMAN COLAB- Silman Structural Solutions'

# KEY DICTIONARY
nested_dict = {
    'C2': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '14x14 (8)#11', 'TL': 'Level 4'}],
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
    'C7': [{'BL': 'Level 1', 'SFN': '18x18 (12)#10', 'TL': 'Level 2'}, {'BL': 'Level 2', 'SFN': '18x18 (12)#10', 'TL': 'Level 4'}]
}

# Reorganize the dictionary
reorganized_dict = {}

for key in sorted(nested_dict.keys(), key=lambda x: (int(x[1:]), x[0])):
    reorganized_dict[key] = nested_dict[key]

# Print the reorganized dictionary
print(reorganized_dict)
