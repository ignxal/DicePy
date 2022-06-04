import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "
IS_FIRST_ITERATION = True

def parse_input(input_string):
    """
    Check if `input_string` is an integer higher than 1.
    If so, return an integer with the same value.
    Else, warn user and quit the program.
    """
    
    try:
        integer = int(input_string.strip())
        if integer>0:
            return integer
        else:
            print("Please enter a value higher than 1")
            raise SystemExit(1)        
    except ValueError:
        print("Please enter a positive integer")
        raise SystemExit(1)

def roll_dice(num):
    """
    Return a list of integers with length `num`.
    """
    results = []
    for _ in range(num):
        roll = random.randint(1, 6)
        results.append(roll)
    return results

def generate_dice_faces_diagram(dice_values):
    """
    Return an ASCII diagram of dice faces from `dice_values`.

    For example, if `dice_values = [4, 1, 3, 2]` then the string
    returned looks like this:

    ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘
    """
    global IS_FIRST_ITERATION
    dice_faces = _get_dice_faces(dice_values)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)
    dice_faces_diagram = "\n".join(dice_faces_rows)

    if IS_FIRST_ITERATION:
        width = len(dice_faces_rows[0])
        diagram_header = " RESULTS ".center(width, "~")
        dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
        IS_FIRST_ITERATION = False

    return dice_faces_diagram

def _get_dice_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces

def _generate_dice_faces_rows(dice_faces):
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []    
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows

############################ MAIN ############################ 

# Get Input
num_input = input("Write the amount of dices to be rolled: ")
num = parse_input(num_input)

# Let's rock&roll
roll_results = roll_dice(num)

while len(roll_results) > 0:
    # Generate ASCII diagram
    dice_face_diagram = generate_dice_faces_diagram(roll_results[0:8])

    # Display it
    print(f"\n{dice_face_diagram}")
    
    # Remove elements already displayed
    del roll_results[0:8]