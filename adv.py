from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

def path_finder(player):
    steps = [] #traversal path
    visited = set()

    stack_traversal = Stack()

    current_room = world.rooms[0]

    while len(visited) < len(world.rooms):
        visited.add(current_room)

        remaining_choices = []

        if current_room.n_to is not None and current_room.n_to not in visited:
            remaining_choices.append('n')

        if current_room.s_to is not None and current_room.s_to not in visited:
            remaining_choices.append('s')

        if current_room.e_to is not None and current_room.e_to not in visited:
            remaining_choices.append('e')

        if current_room.w_to is not None and current_room.w_to not in visited:
            remaining_choices.append('w')


        if len(remaining_choices) == 0:
            last_move = stack_traversal.pop()
            if last_move == 'n':
                current_room = current_room.s_to
                steps.append('s')
            if last_move == 's':
                current_room = current_room.n_to
                steps.append('n')
            if last_move == 'e':
                current_room = current_room.w_to
                steps.append('w')
            if last_move == 'w':
                current_room = current_room.e_to
                steps.append('e')
       
        if len(remaining_choices) > 0:
            choice = random.choice(remaining_choices)
            steps.append(choice)
            stack_traversal.push(choice)
            if choice == 'n':
                current_room = current_room.n_to
            
            if choice == 's':
                current_room = current_room.s_to

            if choice == 'w':
                current_room = current_room.w_to
            
            if choice == 'e':
                current_room = current_room.e_to
    return steps                      


            



# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# random.seed(28187)
traversal_path = path_finder(player)



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
