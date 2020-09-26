"""
Write most of my code here

neighbor: any adjacent room - each room has a function. Get exits. You can use the rooms themselves to figure out where to go next without the player

Algo:
start from room 0, discover the entire set of rooms. When you go North: populate that value of the room --> Adjacency list. Done if I have 500 keys and no question marks. 

1. Use BFS when stuck to find empty room - not explored yet. Can't find one? Done with searching. If you use player, you might get lost. Do BFS first on all the rooms without the player (Human can't move BFS way). Those are the paths -->

2. Use DFT in general - no more door to go to, at the end of the traversal. You can't teleport from one room to another. Gotta back track from current room to the unvisited room. You need to know when to end or start a traversal. I can use the player here. 

"""
# random is a built-in library of python we will use to generate random points
import random
from room import Room
from player import Player
from world import World
from graph import Graph
from util import Stack
from ast import literal_eval

# Load world - 1. pulling in from the world generation code
world = World()

# You may uncomment the smaller graphs for development and testing purposes.

# Output: TESTS PASSED: 3 moves, 3 rooms visited
# map_file = "maps/test_line.txt"

# Output: TESTS PASSED: 15 moves, 9 rooms visited
# map_file = "maps/test_cross.txt"

# Output: TESTS PASSED: 21 moves, 12 rooms visited
# map_file = "maps/test_loop.txt"

"""
Output: You cannot move in that direction.
You cannot move in that direction.
You cannot move in that direction.
TESTS FAILED: INCOMPLETE TRAVERSAL
2 unvisited rooms
"""
map_file = "maps/test_loop_fork.txt"

# * __2__: Tests pass with `len(traversal_path) <= 2000`
# Output: TESTS PASSED: 997 moves, 500 rooms visited
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# 2. An incomplete list of directions. Your task is to fill this with valid traversal directions
# Fill this out with directions to walk, when walked in order, will visit every room on the map at least once
# traversal_path = ['n', 'n']
"""
Traverse maze in a DFT

To solve this path, you'll want to construct your own traversal graph. You start in room `0`, which contains exits `['n', 's', 'w', 'e']`. Your starting graph should look something like this:
    ```
    {
        0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
    }
    ```
You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful
"""
def build_path(graph):
    # stack that contains our current path
    s = Stack()
    # array that contains our returned paths
    moves = []
    # helps us determine if we hit a dead end
    visited = set()
    # initialize traversal with the 0 index room
    s.push(0)
   
    while len(visited) < len(graph):
        # get the id of the current room in the Stack
        id = s.tail()
        # mark as visited room/vertex/node
        visited.add(id)
        # get information of the current room (tuple data)
        current_room = graph[id]
        # dictionary of possible moves
        rooms_dict = current_room[1]
        # array to track if a room has not been visited yet
        undiscovered = []
        # store undiscovered rooms in relationship to the current room
        for direction, room_id in rooms_dict.items():
            if room_id not in visited:
                undiscovered.append(room_id)
        # assign the next room
        # if we reched a dead end, back track
        if len(undiscovered) > 0:
            next_room = undiscovered[0]
            s.push(next_room)
        else:
            s.pop()
            next_room = s.tail()
           
        # survey the rooms around our current room. 
        for direction, adjacent_id in rooms_dict.items():
            # If the next move matches the room_id,
            if adjacent_id == next_room:
                # add that to move and walk
                moves.append(direction)
    
    return moves

traversal_path = build_path(room_graph)


# def build_traversal(player, traversal_path):
    # create a graph class - pulling in from graph file
#     graph = Graph()
    
#     for i in player.current_room.get_exists():
#         print("FROM FUNCTION: ", i)
        
# build_traversal(player, traversal_path)


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
# UNCOMMENT TO WALK AROUND - REPL code to walk around the map
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
