# Cameron Davis
# IT-140
# Text Based Dungeon Game Final Project

rooms = {  # Room Dictionary
    'Central Control Room': {'Item': 1, 'North': 'Waste Reclamation Facility',
                             'South': 'Armoury', 'East': 'Hangar', 'West': 'Crew Quarters'},
    'Waste Reclamation Facility': {'Item': 1, 'South': 'Central Control Room', 'East': 'Scrap Pile'},
    'Crew Quarters': {'Item': 1, 'East': 'Central Control Room'},
    'Scrap Pile': {'Item': 1, 'West': 'Waste Reclamation Facility'},
    'Armoury': {'Item': 1, 'North': 'Central Control Room', 'East': 'Mainframe'},
    'Mainframe': {'Item': 1, 'West': 'Armoury'},
    'Hangar': {'Item': 1, 'North': 'Exit', 'West': 'Central Control Room'},
    'Exit': {'Item': 1, 'South': 'Hangar'}
}

# Global variable declarations
cur_room = 'Central Control Room'
item_count = 0
game_status = 1
command = []


def changeroom():  # Function to change rooms
    global cur_room
    for room in rooms:
        if room == cur_room:
            for direction in rooms[room]:
                if direction.lower() == command[1].lower():
                    cur_room = rooms[room][direction]


def getitem():  # Function to get items
    global item_count
    for room in rooms:
        if (room == cur_room) and (rooms[room]['Item'] == 1):
            rooms[room]['Item'] = 0
            item_count += 1


def getstatus():  # function to display current status
    # status statements
    print("You are currently in the", cur_room)
    print('You have', item_count, 'data wafers.')

    if rooms[cur_room]['Item'] == 1:  # notification of item in room
        print("There is an undiscovered item in this room\n"
              "You may get item")

    for room in rooms[cur_room]:  # notification of directions that may be moved in
        if (room == 'North') or (room == 'South') or (room == 'East') or (room == 'West'):
            print("You may move", room)


def gameintro():  # one-time introduction paragraph
    print("It is the fifty-first century, and you are an adept of the Order of Red,\n"
          "an organization devoted to techno-archaeology. You have gotten separated\n"
          "from your fellow adepts and have become trapped in an ancient facility deep\n"
          "below the surface of an abandoned planet. The only exit is guarded by an\n"
          "automated defense system. You are unsure if the weapons are still\n"
          "functional, but you have no desire to test it with your life.\n"
          "Gather 7 data-wafers and compile them into a virus to disable\n"
          "the system so you may escape!\n")


def endconditions():  # Win/lose condition logic
    if cur_room == 'Exit':
        if item_count < 6:
            print('You enter the exit.\n'
                  'The defense system activates and shoots you. \n\n'
                  'Game Over')
            return 0
        else:
            print('You enter the exit.\n'
                  'You use the data wafers to deactivate the defense system and escape!\n\n'
                  'You Win!')
            return 0
    else:
        return 1


def main():  # main function definition
    global command
    global item_count
    global game_status

    gameintro()

    while game_status:  # game logic loop contained in while loop

        getstatus()

        command = input("Enter your Command: ").split()  # command input split into tuple

        if command[0].lower() == 'exit':  # conditionals and iterators that control game logic
            break
        elif command[0].lower() == 'move':
            changeroom()
        elif command[0].lower() == 'get':
            getitem()
        else:
            print("Invalid command, please check for spelling.")

        game_status = endconditions()  # win/lose condition check


main()  # main function call
