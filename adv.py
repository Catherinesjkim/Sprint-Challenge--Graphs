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

# Output - TESTS PASSED: 6 moves, 3 rooms visited
map_file = "maps/test_line.txt"

# Output - TESTS PASSED: 18 moves, 9 rooms visited
# map_file = "maps/test_cross.txt"

# Output - TESTS PASSED: 24 moves, 12 rooms visited
# map_file = "maps/test_loop.txt"


# Output - TESTS PASSED: 36 moves, 18 rooms visited
# map_file = "maps/test_loop_fork.txt"

# * __2__: Tests pass with `len(traversal_path) <= 2000`
# Output - TESTS PASSED: 1000 moves, 500 rooms visited
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

Assume that the grid is unweighted and cells connect left, right, up and down

A common approach to solving graph theory problems on grids is to first convert the grid to a familiar format such as an adjacency list/matrix

User direction vector technique

1. BFS
2. DFT
"""
# First, label the cells in the grid with numbers [0, n] where n = #rows x #columns - 0 to 6 non-inclusive (0 - 5)
# Start at the start node coordinate by adding (sr, sc) to the queue
# Then, we visit the adjacent unvisited neighbors and add them to the queue
# If we have reached the end, and if we had a 2D prev matrix, we could regenerate the path by retracing our steps
"""
Plan:
move player into starting room
find all possible exits for room
move in a direction and repeat this process

Plan to keep track of visited rooms/paths
Set direction for reverse as well

Based on this problem: storage space isnt an issue, getting this task accomplished quickly and as efficiently as possible is the main goal. For this, DFS(t) is most likely the ideal solution. 
"""

reverse_move = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

def dftr_maze(current_room, visited=None):
    # list directions while moving
    directions = []
    # creating a set to hold visited rooms if visited is None
    if visited == None:
        visited = set()
        
    # finding exits for current_room using player from player and get_exits from room
    for move in player.current_room.get_exits():
        # making moves using travel from player
        player.travel(move)
        
        # reverse_move if already visited to find new path
        if player.current_room in visited:
            player.travel(reverse_move[move])
        # if its a new room, do the following
        else:
            # add to visited stack
            visited.add(player.current_room)
            # adding this move to 'directions'
            directions.append(move)
            # recursive: repeating loop and adding directions ('\' is an escape character in Python)
            directions = directions + \
                dftr_maze(player.current_room, visited)
            # go_back to previous room
            player.travel(reverse_move[move])
            # appending this move to 'directions'
            directions.append(reverse_move[move])
            
    return directions

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = dftr_maze(player.current_room)
print(dftr_maze)


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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
