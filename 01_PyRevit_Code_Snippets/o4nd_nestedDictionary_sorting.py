__doc__ = "This is a Code snippet for sorting nested dictionary twice first by level names then by mark names. " \
          "After processing plot the data " \
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


# Input Dictionary to sort
originalDict = {'LEVEL 10': [],
                'EMR No.1 LEVEL': [],
                'LEVEL 07': [],
                'BULKHEAD ROOF': [],
                'ROOF LEVEL': ['C68-C# - 48X61 (8) #8', 'C69-C# - 48X61 (8) #8', ],
                'LEVEL 12': [],
                'LEVEL 02': ['C68-C# - 48X61 (8) #8', 'C68-C# - 48x64 (16) #9', 'C69-C# - 48X61 (8) #8',
                              'C69-C# - 48X61 (8) #8'],
                'LEVEL 09': ['C50-C# - 36"x12 (8) #8', 'C22-C# - 32"x12" (16) #9', 'C22-C# - 20"x12" (12) #10',
                              'C21-C# - 40"x12" (12) #10', 'C21-C# - 26"x12" (12) #8'],
                'LEVEL 11': [],
                'LEVEL 01': ['C68-C# - 48x64 (16) #9', 'C68-C# - 48x64 (16) #9', 'C56-C# - 64x48 (12) #10',
                              'C56-C# - 64x48 (12) #10'],
                'UPPER MECH. PLATFORM': ['C16-C# - 12x12 (8) #8', 'C14-C# - 12x12 (8) #8',
                                          'C35-C# - 16x18 (16) #9', 'C32-C# - 12x16 (8) #8'],
                'LEVEL 14': ['C50-C# - 36"x12 (8) #8', 'C50-C# - 24x12 (12) #10', 'C57-C# - 20x20 (16) #9',
                             'C25-C# - 20x20 (16) #9', 'C14-C# - 36"x12 (8) #8'],
                'LEVEL 04': ['C57-C# - 24x24 (12) #10', 'C57-C# - 20x20 (16) #9', 'C25-C# - 20x20 (16) #9',
                             'C25-C# - 33" (14) #9', 'C37-C# - 48x16 (16) #9'],
                'LEVEL 00 - CELLAR': ['C68-C# - 48x64 (16) #9', 'C69-C# - 48X61 (8) #8', 'C7-C# - 12x24 (12) #8',
                                       'C56-C# - 64x48 (12) #10', 'C54-C# - 12x24 (12) #8'],
                'T.O. EXIST. ROOF SLAB': [],
                'LEVEL 13': [],
                'LEVEL 03': ['C69-C# - 48X61 (8) #8', 'C69-C# - 48X61 (8) #8', 'C55-C# - 12x28 (12) #8',
                             'C24-C# - 12x24 (12) #8'],
                'T.O. SCREEN WALL': [],
                'LOWER MECH. PLATFORM': [],
                'T.O. SLAB BEFORE SLOPE': [],
                'LEVEL 06': [],
                'Survey': [],
                'LEVEL 05': ['C46-C# - 64x12 (12) #8', 'C44-C# - 74x12 (12) #10', 'C44-C# - 58x12 (12) #8',
                             'C47-C# - 52x12 (12) #10'],
                'LEVEL 08': [],
                'Ground Floor': ['C52-C# - 18"x72" (12) #10', 'C57-C# - 24x24 (12) #10'],
                'ELEV. No.2 LEVEL': ['C43-C# - 12x12 (8) #8', 'C47-C# - 12x12 (8) #8', 'C62-C# - 12x12 (8) #8']}

# Optional Dictionary to sort
originalDict1 = {'LEVEL 10': [], 'EMR No.1 LEVEL': [], 'LEVEL 07': [], 'BULKHEAD ROOF': [], 'ROOF LEVEL': ['C68-C# - 48X61 (8) #8', 'C69-C# - 48X61 (8) #8', 'C56-C# - 48x48 (8) #8', 'C53-C# - 48x48 (8) #8', 'C50-C# - 12x12 (8) #8', 'C50-C# - 24x12 (12) #10', 'C26-C# - 48x48 (8) #8', 'C22-C# - 12x12 (8) #8', 'C22-C# - 20"x12" (12) #10', 'C20-C# - 48X61 (8) #8', 'C21-C# - 12x12 (8) #8', 'C21-C# - 26"x12" (12) #8', 'C29-C# - 48x48 (8) #8', 'C16-C# - 26"x12" (12) #8', 'C16-C# - 12x12 (8) #8', 'C14-C# - 12x12 (8) #8', 'C14-C# - 24x12 (12) #10', 'C17-C# - 48X61 (8) #8', 'C43-C# - 24x12 (12) #10', 'C43-C# - 12x12 (8) #8', 'C47-C# - 24x12 (12) #10', 'C47-C# - 12x12 (8) #8', 'C37-C# - 40"x12" (12) #10', 'C37-C# - 12x12 (8) #8', 'C35-C# - 16x18 (16) #9', 'C35-C# - 26"x16 (16) #9', 'C32-C# - 12x16 (8) #8', 'C32-C# - 24x16 (12) #8', 'C48-C# - 12x12 (8) #8', 'C48-C# - 24x12 (12) #10', 'C38-C# - 30"x12" (12) #8', 'C38-C# - 12x12 (8) #8', 'C66-C# - 12x12 (8) #8', 'C66-C# - 30"x12" (12) #8', 'C67-C# - 12x12 (8) #8', 'C67-C# - 26"x12" (12) #8', 'C62-C# - 26"x12" (12) #8', 'C62-C# - 12x12 (8) #8', 'C63-C# - 30"x12" (12) #8', 'C63-C# - 12x12 (8) #8'], 'LEVEL 12': [], 'LEVEL 02': ['C68-C# - 48X61 (8) #8', 'C68-C# - 48x64 (16) #9', 'C69-C# - 48X61 (8) #8', 'C69-C# - 48X61 (8) #8', 'C7-C# - 12x24 (12) #8', 'C56-C# - 48x48 (8) #8', 'C56-C# - 64x48 (12) #10', 'C55-C# - 12x28 (12) #8', 'C55-C# - 12x28 (12) #8', 'C52-C# - 18"x72" (12) #10', 'C53-C# - 48x48 (8) #8', 'C53-C# - 52x50 (12) #10', 'C51-C# - 67x36 (16) #9', 'C26-C# - 48x48 (8) #8', 'C26-C# - 50x53 (12) #10', 'C24-C# - 12x24 (12) #8', 'C22-C# - 32"x12" (16) #9', 'C22-C# - 92"x12 (12) #8', 'C20-C# - 48X61 (8) #8', 'C20-C# - 48X61 (8) #8', 'C21-C# - 40"x12" (12) #10', 'C28-C# - 12x28 (12) #8', 'C28-C# - 12x28 (12) #8', 'C29-C# - 48x48 (8) #8', 'C29-C# - 66x52 (16) #9', 'C16-C# - 32"x12" (16) #9', 'C14-C# - 42"x12 (14) #9', 'C15-C# - 80x12 (12) #10', 'C17-C# - 48X61 (8) #8', 'C17-C# - 48X61 (8) #8', 'C19-C# - 12x24 (12) #8', 'C19-C# - 12x24 (12) #8', 'C46-C# - 64x12 (12) #8', 'C44-C# - 74x12 (12) #10', 'C45-C# - 12x160 (12) #10', 'C37-C# - 48x16 (16) #9', 'C33-C# - 112x16 (16) #9', 'C33-C# - 9\'-4"X1\'4-" (14) #9', 'C30-C# - 12x24 (12) #8', 'C31-C# - 18"x72" (12) #10', 'C8-C# - 12x24 (12) #8', 'C48-C# - 58x12 (12) #8', 'C49-C# - 58x12 (12) #8', 'C38-C# - 50x12 (12) #8', 'C66-C# - 44"x12 (14) #9', 'C66-C# - 50"x24" (12) #10', 'C67-C# - 38"x12 (12) #8', 'C65-C# - 12x26 (12) #8', 'C65-C# - 12x26 (12) #8', 'C62-C# - 38"x12 (12) #8', 'C62-C# - 48"x22" (12) #8', 'C63-C# - 44"x12 (14) #9'], 'LEVEL 09': ['C50-C# - 36"x12 (8) #8', 'C22-C# - 32"x12" (16) #9', 'C22-C# - 20"x12" (12) #10', 'C21-C# - 40"x12" (12) #10', 'C21-C# - 26"x12" (12) #8', 'C16-C# - 26"x12" (12) #8', 'C16-C# - 32"x12" (16) #9', 'C14-C# - 42"x12 (14) #9', 'C14-C# - 36"x12 (8) #8', 'C44-C# - 58x12 (12) #8', 'C43-C# - 48x12 (8) #8', 'C47-C# - 52x12 (12) #10', 'C47-C# - 42"x12 (14) #9', 'C37-C# - 40"x12" (12) #10', 'C37-C# - 48x14 (14) #9', 'C34-C# - 50x16 (12) #8', 'C34-C# - 44"x16 (8) #8', 'C32-C# - 38"x16 (16) #9', 'C32-C# - 34"x16 (8) #8', 'C48-C# - 46x12 (12) #10', 'C48-C# - 36"x12 (8) #8', 'C49-C# - 46x12 (12) #10', 'C38-C# - 50x12 (12) #8', 'C38-C# - 30"x12" (12) #8', 'C66-C# - 44"x12 (14) #9', 'C66-C# - 30"x12" (12) #8', 'C67-C# - 38"x12 (12) #8', 'C67-C# - 26"x12" (12) #8', 'C62-C# - 38"x12 (12) #8', 'C62-C# - 26"x12" (12) #8', 'C63-C# - 30"x12" (12) #8', 'C63-C# - 44"x12 (14) #9'], 'LEVEL 11': [], 'LEVEL 01': ['C68-C# - 48x64 (16) #9', 'C68-C# - 48x64 (16) #9', 'C56-C# - 64x48 (12) #10', 'C56-C# - 64x48 (12) #10', 'C54-C# - 12x24 (12) #8', 'C55-C# - 12x28 (12) #8', 'C55-C# - 18x28 (14) #9', 'C52-C# - 72"x36 (12) #10', 'C53-C# - 52x50 (12) #10', 'C53-C# - 52x50 (12) #10', 'C2-C# - 12x24 (12) #8', 'C58-C# - 12x12 (8) #8', 'C59-C# - 12x12 (8) #8', 'C9-C# - 12x24 (12) #8', 'C1-C# - 12x24 (12) #8', 'C26-C# - 52x53 (14) #9', 'C26-C# - 50x53 (12) #10', 'C27-C# - 12x24 (12) #8', 'C25-C# - 33" (14) #9', 'C22-C# - 92"x12 (12) #8', 'C23-C# - 51"x24" (12) #10', 'C4-C# - 14x24 (14) #9', 'C28-C# - 24x24 (12) #10', 'C28-C# - 12x28 (12) #8', 'C29-C# - 68x52 (16) #9', 'C29-C# - 66x52 (16) #9', 'C3-C# - 12x24 (12) #8', 'C15-C# - 84x12 (12) #10', 'C15-C# - 80x12 (12) #10', 'C12-C# - 16x24 (16) #9', 'C13-C# - 12x12 (8) #8', 'C10-C# - 12x24 (12) #8', 'C11-C# - 12x24 (12) #8', 'C17-C# - 48X62 (16) #9', 'C17-C# - 48X61 (8) #8', 'C18-C# - 12x24 (12) #8', 'C19-C# - 12x24 (12) #8', 'C19-C# - 18x24 (12) #8', 'C6-C# - 12x24 (12) #8', 'C45-C# - 13\' 4"\'X1\'-0" (12) #10', 'C45-C# - 12x160 (12) #10', 'C42-C# - 12x24 (12) #8', 'C40-C# - 12x24 (12) #8', 'C33-C# - 9\'-4"X1\'4-" (14) #9', 'C33-C# - 9\'-4"X1\'4-" (14) #9', 'C30-C# - 12x24 (12) #8', 'C31-C# - 72"x36 (12) #10', 'C31-C# - 18"x72" (12) #10', 'C5-C# - 14x24 (14) #9', 'C66-C# - 56"x24" (12) #8', 'C67-C# - 12x24 (12) #8', 'C64-C# - 12x24 (12) #8', 'C65-C# - 36"x12 (8) #8', 'C65-C# - 12x26 (12) #8', 'C62-C# - 48"x24" (12) #8', 'C62-C# - 48"x22" (12) #8', 'C60-C# - 12x12 (8) #8'], 'UPPER MECH. PLATFORM': ['C16-C# - 12x12 (8) #8', 'C14-C# - 12x12 (8) #8', 'C35-C# - 16x18 (16) #9', 'C32-C# - 12x16 (8) #8'], 'LEVEL 14': ['C50-C# - 36"x12 (8) #8', 'C50-C# - 24x12 (12) #10', 'C57-C# - 20x20 (16) #9', 'C25-C# - 20x20 (16) #9', 'C14-C# - 36"x12 (8) #8', 'C14-C# - 24x12 (12) #10', 'C43-C# - 48x12 (8) #8', 'C43-C# - 24x12 (12) #10', 'C47-C# - 42"x12 (14) #9', 'C47-C# - 24x12 (12) #10', 'C34-C# - 44"x16 (8) #8', 'C35-C# - 26"x16 (16) #9', 'C32-C# - 34"x16 (8) #8', 'C32-C# - 24x16 (12) #8', 'C48-C# - 36"x12 (8) #8', 'C48-C# - 24x12 (12) #10', 'C39-C# - 20x20 (16) #9', 'C61-C# - 20x20 (16) #9'], 'LEVEL 04': ['C57-C# - 24x24 (12) #10', 'C57-C# - 20x20 (16) #9', 'C25-C# - 20x20 (16) #9', 'C25-C# - 33" (14) #9', 'C37-C# - 48x16 (16) #9', 'C37-C# - 48x14 (14) #9', 'C39-C# - 20x20 (16) #9', 'C39-C# - 24x24 (12) #10', 'C61-C# - 24x24 (12) #10', 'C61-C# - 20x20 (16) #9'], 'LEVEL 00 - CELLAR': ['C68-C# - 48x64 (16) #9', 'C69-C# - 48X61 (8) #8', 'C7-C# - 12x24 (12) #8', 'C56-C# - 64x48 (12) #10', 'C54-C# - 12x24 (12) #8', 'C55-C# - 18x28 (14) #9', 'C52-C# - 72"x36 (12) #10', 'C53-C# - 52x50 (12) #10', 'C51-C# - 67x36 (16) #9', 'C2-C# - 12x24 (12) #8', 'C58-C# - 12x12 (8) #8', 'C59-C# - 12x12 (8) #8', 'C9-C# - 12x24 (12) #8', 'C1-C# - 12x24 (12) #8', 'C26-C# - 52x53 (14) #9', 'C27-C# - 12x24 (12) #8', 'C23-C# - 51"x24" (12) #10', 'C20-C# - 48X61 (8) #8', 'C4-C# - 14x24 (14) #9', 'C28-C# - 24x24 (12) #10', 'C29-C# - 68x52 (16) #9', 'C3-C# - 12x24 (12) #8', 'C15-C# - 84x12 (12) #10', 'C12-C# - 16x24 (16) #9', 'C10-C# - 12x24 (12) #8', 'C11-C# - 12x24 (12) #8', 'C17-C# - 48X62 (16) #9', 'C18-C# - 12x24 (12) #8', 'C19-C# - 18x24 (12) #8', 'C6-C# - 12x24 (12) #8', 'C45-C# - 13\' 4"\'X1\'-0" (12) #10', 'C42-C# - 12x24 (12) #8', 'C40-C# - 12x24 (12) #8', 'C41-C# - 12x12 (8) #8', 'C36-C# - 12x12 (8) #8', 'C33-C# - 9\'-4"X1\'4-" (14) #9', 'C30-C# - 12x24 (12) #8', 'C31-C# - 72"x36 (12) #10', 'C5-C# - 14x24 (14) #9', 'C8-C# - 12x24 (12) #8', 'C66-C# - 56"x24" (12) #8', 'C67-C# - 12x24 (12) #8', 'C64-C# - 12x24 (12) #8', 'C65-C# - 36"x12 (8) #8', 'C62-C# - 48"x24" (12) #8', 'C60-C# - 12x12 (8) #8'], 'T.O. EXIST. ROOF SLAB': [], 'LEVEL 13': [], 'LEVEL 03': ['C69-C# - 48X61 (8) #8', 'C69-C# - 48X61 (8) #8', 'C55-C# - 12x28 (12) #8', 'C24-C# - 12x24 (12) #8', 'C28-C# - 12x28 (12) #8', 'C13-C# - 12x12 (8) #8', 'C19-C# - 12x24 (12) #8', 'C30-C# - 12x24 (12) #8', 'C65-C# - 12x26 (12) #8'], 'T.O. SCREEN WALL': [], 'LOWER MECH. PLATFORM': [], 'T.O. SLAB BEFORE SLOPE': [], 'LEVEL 06': [], 'Survey': [], 'LEVEL 05': ['C46-C# - 64x12 (12) #8', 'C44-C# - 74x12 (12) #10', 'C44-C# - 58x12 (12) #8', 'C47-C# - 52x12 (12) #10', 'C34-C# - 50x16 (12) #8', 'C32-C# - 38"x16 (16) #9', 'C33-C# - 112x16 (16) #9', 'C48-C# - 58x12 (12) #8', 'C48-C# - 46x12 (12) #10', 'C49-C# - 58x12 (12) #8', 'C49-C# - 46x12 (12) #10'], 'LEVEL 08': [], 'Ground Floor': ['C52-C# - 18"x72" (12) #10', 'C57-C# - 24x24 (12) #10', 'C41-C# - 12x12 (8) #8', 'C36-C# - 12x12 (8) #8', 'C39-C# - 24x24 (12) #10', 'C66-C# - 50"x24" (12) #10', 'C61-C# - 24x24 (12) #10'], 'ELEV. No.2 LEVEL': ['C43-C# - 12x12 (8) #8', 'C47-C# - 12x12 (8) #8', 'C62-C# - 12x12 (8) #8', 'C63-C# - 12x12 (8) #8']}


# Input Level Names used for dictionary sorting (The elements in the list are in the sequence)
levelsnames = ['T.O. SCREEN WALL', 'UPPER MECH. PLATFORM', 'BULKHEAD ROOF', 'LOWER MECH. PLATFORM', 'ELEV. No.2 LEVEL',
                'ROOF LEVEL', 'T.O. EXIST. ROOF SLAB', 'EMR No.1 LEVEL', 'LEVEL 14', 'LEVEL 13', 'LEVEL 12', 'LEVEL 11',
                'LEVEL 10', 'LEVEL 09', 'LEVEL 08', 'LEVEL 07', 'LEVEL 06', 'LEVEL 05', 'LEVEL 04', 'LEVEL 03', 'LEVEL 02',
                'T.O. SLAB BEFORE SLOPE', 'Ground Floor', 'LEVEL 01', 'LEVEL 00 - CELLAR', 'Survey']

# Mark names used for dictionary sorting (The elements in the list are in the sequence)
marknames = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17',
              'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C27', 'C28', 'C29', 'C30', 'C31', 'C32', 'C33',
              'C34', 'C35', 'C36', 'C37', 'C38', 'C39', 'C40', 'C41', 'C42', 'C43', 'C44', 'C45', 'C46', 'C47', 'C48', 'C49',
              'C50', 'C51', 'C52', 'C53', 'C54', 'C55', 'C56', 'C57', 'C58', 'C59', 'C60', 'C61', 'C62', 'C63', 'C64', 'C65',
              'C66', 'C67', 'C68', 'C69']

# STEP 1 - Sorting the Dictionary by their first outer level keys to match the sequence in the list "levelnames"
sorted_keys = sorted(originalDict1.keys(), key=lambda x: levelsnames.index(x) if x in levelsnames else float('inf'))
sorted_dict = {key: originalDict1[key] for key in sorted_keys}

# We are trying to rearrange the dictionary by the outside keys based on the sequence of items in the list "levelnames"
print("01.Sorting Dictionary of Levels with Mark Names by LevelNames sequence" , sorted_dict)

# STEP 2 - Sorting the Dictionary second time now by the adding marks names as keys, sortedlevelnames as outerlevel keys
# and the values as SFN values with rebar "
# Create a new dictionary with marknames as second levelkeys and values based on originalDict
new_dict = {}
for key, value in sorted_dict.items():
    new_dict[key] = {mark: "" for mark in marknames}

    # Assign values based on the originalDict values
    for element in value:
        mark = element.split('-')[0].strip()  # Extract the mark from the element
        if mark in marknames:
            new_dict[key][mark] = element

print("02.Sorting the Dictionary by their first outer level keys to match the sequence in the list- levelnames : ", new_dict)


# STEP 3 - We just now make a new dictionary to re-arrange the LevelNames as the keys and List of values from the
# previous marknames values stores in a List as values

# Create new_dictionary with empty lists as values for keys
new_dictionary = {key: [''] * len(marknames) for key in new_dict.keys()}

# Populate new_dictionary with values from new_dict
for i, mark in enumerate(marknames):
    for key, value in new_dict.items():
        new_dictionary[key][i] = value.get(mark, '')

print("03.Sorting the dictionary second time by marknames as internal keys and numerical value sorting : ",new_dictionary)

# Expected Output for Step 2
"""
'Ground Floor': {'C1': '', 'C2': '', 'C3': '', 'C4': '', 'C5': '', 'C6': '', 'C7': '', 'C8': '', 'C9': '', 'C10': '', 'C11': '', 'C12': '', 'C13': '', 'C14': '', 'C15': '', 'C16': '', 'C17': '', 'C18': '', 'C19': '', 'C20': '', 'C21': '', 'C22': '', 'C23': '', 'C24': '', 'C25': '', 'C26': '', 'C27': '', 'C28': '', 'C29': '', 'C30': '', 'C31': '', 'C32': '', 'C33': '', 'C34': '', 'C35': '', 'C36': '', 'C37': '', 'C38': '', 'C39': '', 'C40': '', 'C41': '', 'C42': '', 'C43': '', 'C44': '', 'C45': '', 'C46': '', 'C47': '', 'C48': '', 'C49': '', 'C50': '', 'C51': '', 'C52': 'C52-C# - 18"x72" (12) #10', 'C53': '', 'C54': '', 'C55': '', 'C56': '', 'C57': 'C57-C# - 24x24 (12) #10', 'C58': '', 'C59': '', 'C60': '', 'C61': '', 'C62': '', 'C63': '', 'C64': '', 'C65': '', 'C66': '', 'C67': '', 'C68': '', 'C69': ''}
"""

# Expected Output for Step 3
""" 
{'T.O. SCREEN WALL': ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
'Ground Floor': ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','C52-C# - 18x72 (12) #10','','','','','C57-C# - 24x24 (12) #10','','','','','','','','','','','', '']
}

"""


