__doc__ = "This is a Code snippet for Reading through a nested dictionary and list of levels. After processing plot the data " \
          "This was used in Pyrevit Code snippet ConColSchedulerXLView"
__author__ = 'Abhishek Shinde | Silman Colab'
__contact__ = 'abhishek.shinde@silman.com | arabhishek1091@gmail.com'
__copyright__ = 'SILMAN COLAB- Silman Structural Solutions'

"""
CODE LIMITATION
***************
NOTE: This code works with CPython or Python from Anaconda. However, this does not work with Ipython
The reason because older version of Ironpython do not support sorted and key for sorting dictionary
"""


# Input dictionary
CCSXLMarks = {
    'C68': [{'BL': 'LEVEL 00 - CELLAR', 'SFN': 'C# - 48x64 ', 'TL': 'LEVEL 01'}, {'BL': 'LEVEL 02', 'SFN': 'C# - 48X61 ', 'TL': 'ROOF LEVEL'}],
    'C69': [{'BL': 'LEVEL 00 - CELLAR', 'SFN': 'C# - 48X61 ', 'TL': 'LEVEL 02'}, {'BL': 'LEVEL 02', 'SFN': 'C# - 48X74 ', 'TL': 'LEVEL 03'}],
    'C56': [{'BL': 'LEVEL 02', 'SFN': 'C# - 48x48 ', 'TL': 'ROOF LEVEL'}, {'BL': 'LEVEL 00 - CELLAR', 'SFN': 'C# - 64x48 ', 'TL': 'LEVEL 01'}],
    'C57': [{'BL': 'Ground Floor', 'SFN': 'C# - 24x24 (16) #9', 'TL': 'LEVEL 04'}, {'BL': 'LEVEL 04', 'SFN': 'C# - 20x20 (16) #9', 'TL': 'LEVEL 14'}],
    }

print(CCSXLMarks.values())
print("*" * 200)

# Input Levels
LevelstoSearchfor = ['T.O. SCREEN WALL', 'UPPER MECH. PLATFORM', 'BULKHEAD ROOF', 'LOWER MECH. PLATFORM', 'ELEV. No. LEVEL',
                     'ROOF LEVEL', 'T.O. EXIST. ROOF SLAB', 'EMR No.1 LEVEL', 'LEVEL 14', 'LEVEL 13', 'LEVEL 12', 'LEVEL 11',
                     'LEVEL 10', 'LEVEL 09', 'LEVEL 08', 'LEVEL 07', 'LEVEL 06', 'LEVEL 05', 'LEVEL 04', 'LEVEL 03', 'LEVEL 02',
                     'T.O. SLAB BEFORE SLOPE', 'Ground Floor', 'LEVEL 01', 'LEVEL 00 - CELLAR', 'Survey']

print(LevelstoSearchfor[23:])
print("*" * 200)


# Expected output
"""   
T.O. SCREEN WALL = []
UPPER MECH. PLATFORM = []
BULKHEAD ROOF = []
LOWER MECH. PLATFORM = []
ELEV. No. LEVEL = []
ROOF LEVEL = ['C# - 48X61 ','C# - 48x48 ']
T.O. EXIST. ROOF SLAB = ['C# - 48X61 ','C# - 48x48 ']
EMR No.1 LEVEL = ['C# - 48X61 ','C# - 48x48 ']
LEVEL 14 = ['C# - 48X61 ','C# - 48x48 ','C# - 20x20 (16) #9']
LEVEL 13 = ['C# - 48X61 ','C# - 48x48 ','C# - 20x20 (16) #9']
LEVEL 12 = ['C# - 48X61 ','C# - 48x48 ','C# - 20x20 (16) #9']
LEVEL 11 = ['C# - 48X61 ','C# - 48x48 ','C# - 20x20 (16) #9']
LEVEL 10 = ['C# - 48X61 ','C# - 48x48 ','C# - 20x20 (16) #9']
LEVEL 09 = ['C# - 48X61 ','C# - 48x48 ','C# - 20x20 (16) #9']
LEVEL 08 = ['C# - 48X61 ','C# - 48x48 ','C# - 20x20 (16) #9']
LEVEL 07 = ['C# - 48X61 ','C# - 48x48 ','C# - 20x20 (16) #9']
LEVEL 06 = ['C# - 48X61 ','C# - 48x48 ','C# - 20x20 (16) #9']
LEVEL 05 = ['C# - 48X61 ','C# - 48x48 ','C# - 20x20 (16) #9']
LEVEL 04 = ['C# - 48X61 ','C# - 48x48 ','C# - 24x24 (16) #9','C# - 20x20 (16) #9']
LEVEL 03 = ['C# - 48X61 ','C# - 48X74 ','C# - 48x48 ','C# - 24x24 (16) #9' ]
LEVEL 02 = ['C# - 48X61 ',C# - 48X61 ','C# - 48X74 ','C# - 48x48 ','C# - 24x24 (16) #9']
T.O. SLAB BEFORE SLOPE = [C# - 48X61 ','C# - 24x24 (16) #9']
Ground Floor = [C# - 48X61 ','C# - 24x24 (16) #9']
LEVEL 01 = ['C# - 48x64 ',C# - 48X61 ','C# - 64x48 ']
LEVEL 00 - CELLAR = ['C# - 48x64 ',C# - 48X61 ','C# - 64x48 ']
Survey = []
"""

# Function to Process Column Marks information based on Level Ranges
def process_levels(levelstosearchfor, concretecolumnmarksDict):
    result = {level: [] for level in levelstosearchfor}

    for key, values in concretecolumnmarksDict.items():
        for value in values:
            #print(value['SFN'])
            #b1_level = int(value["BL"].split()[-1])
            b1_level = value["BL"].strip()# Strip leading and trailing spaces
            #t1_level = int(value["TL"].split()[-1])
            t1_level = value["TL"].strip()# Strip leading and trailing spaces
            #for level in range(b1_level, t1_level + 1): result["Level {}".format(level)].append(value["SFN"])
            # If both b1_level and t1_level are valid levels ie. they  are in levelstosearchfor , append "SFN"
            if b1_level in levelstosearchfor and t1_level in levelstosearchfor:
                # Find the index of BL and TL in levelstosearchfor
                b1_levelindex = levelstosearchfor.index(b1_level)
                t1_levelindex = levelstosearchfor.index(t1_level)
                print("Index of b1_level is ", b1_levelindex)
                print("Index of t1_level is", t1_levelindex)
                print(f"Processing column with schedule mark {key} starting from {b1_level} to {t1_level}")
                print("SFN Value for the Processing key and its level is ",value['SFN'])
                print("*" * 200)
                # Iterate over the levels between BL and TL (inclusive)
                # for level in range(index_b1, index_t1 + 1):
                # for level in levelstosearchfor[b1_levelindex:t1_levelindex + 1]:
                for level in levelstosearchfor[:]:
                    index_level = levelstosearchfor.index(level)
                    # Check if the current level is within the range
                    if level == b1_level or t1_level == level or (index_level > levelstosearchfor.index(b1_level) and index_level < levelstosearchfor.index(t1_level)):
                        result[level].append(value["SFN"])
                    #print('Level',level)
                    #print(levelstosearchfor[b1_levelindex:t1_levelindex])
                    # result[levelstosearchfor[level]] += [value["SFN"]]
                    #result[level] += [value['SFN']]
                    #result[level].append(value["SFN"])
            else:
                print(f"Error: Invalid value for BL or TL level - BL: {b1_level}, TL: {t1_level}")

    #for level, values in result.items(): print(f"{level} = {values}")
    return result

# Final Output for Processing Level and Marks information
final_output = process_levels(LevelstoSearchfor, CCSXLMarks)

# Print the final output
for level, values in final_output.items():
    print("{} = {}".format(level, values))

print("*" * 200)
#print(type(final_output))
#print("*" * 200)
