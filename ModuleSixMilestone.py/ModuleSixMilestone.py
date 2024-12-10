#Brian Engel

#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'south': 'Bedroom'},
        'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
        'Cellar': {'west': 'Bedroom'}
    }
#function for moving between rooms
def move_between_rooms(current_room, direction):
    #if the direction is valid to move rooms then set room to new room
    if direction in rooms[current_room]:
        new_current_room = rooms[current_room][direction]
    #if the direction is 'exit' change room to exit
    elif direction == 'exit':
        new_current_room = 'exit'
    # if the direction is not valid stay in the same room
    else:
        new_current_room = current_room
        print('invalid command')
    #return the room to the program
    return new_current_room

#function to get user input and return it in a uniform manner
def user_input(current_room):
    #set initial value for command as nothing
    user_command = ''
    #while nothing has been input the loop will repeat
    while user_command == '':
        #input from user
        user_command = input('Enter a command:')
        #strips any extra space of the beginning and end of string
        user_command = user_command.strip()
        #if nothing was input let user know invalid
        if user_command == '':
            print('invalid command')
    #changes entire string to lowercase to prevent errors
    user_command = user_command.lower()
    #returns stripped down lowercase version of what user typed
    return user_command

#set an initial room
room = 'Bedroom'
'''while the room is set to a room in the dictionary it will loop (once exit is typed 
exit is assigned to the room and since it's not in the dictionary it will exit)
'''
while room in rooms:
    # print current location and command options
    print('You are in the ', current_room)
    print('To move rooms type North, South, East, or West.')
    print('Type \'exit\' to exit')
    direction = user_input(room)
    room = move_between_rooms(room, direction)