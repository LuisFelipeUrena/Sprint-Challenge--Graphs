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

def path_finder(player, world):
    # first we have to start at a certain room which will be room 0
    player.current_room = world.starting_room
    # then we instantiate a visited rooms set
    visited = set()
    # then we instantiate a stack
    to_visit = Stack()
    # add the first room to the stack
    to_visit.push(player.current_room.id)
    # create a steps list
    steps = []
    # start traversing thru the graph
    while to_visit.size() > 0:
        # take the top of the stack
        v = to_visit.pop()
        # if the v is not visited yet, add it
        if v not in visited:
            visited.add(v)
        # for each valid move in the current room
        for move in player.current_room.get_exits():
            player.travel(move)
            to_visit.push(player.current_room.id)
            steps.append(move)
    return steps        




# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = path_finder(player,world)



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
