"""
* Fill out a list with traversal that will visit all rooms at least once

* Commands:
    - player.current_room.id: This will give us the current room id
    
    - plyer.current_room.get_exists(): Will return a list of possible moves we can make
    
    - player.travel(direction, [boolean: will display room info to us]): This will allow us to move / traverse visited_rooms
    
* Create an array with a valid move set: We can achieve this with the player.current_room.get_exists()

* Graph Class
    - Will need a vertices attribute that is a dictionary (complete)
        - the keys will be a room id
        - the values will be a dict, this will hold n, s, e, w whose values will be the room id for the possible move
    - The vertex will be the curren room id
    - The edges will be the rooms that the room ID connects to
    - Some function: We will need the player instance passed to us so that we have a way to move around the Player
    - We need a BFT function for us to move around and traverse the map
"""

class Graph:
    
    # init a graph
    def __init__(self):
        self.vertices = {}
    
    """
    Add a vertex to the graph
    """
    def add_vertex(self, vertex):
        # the vertex passed to us is going to be a room id number
        if vertex not in self.vertices:
            self.vertices[vertex] = {'n': '?', 's': '?', 'e': '?', 'w': '?'}
            
            
    """
    Add an edge to the vertex
    
    The vertex passed should be a room id
    The key passed should be a string of n, s, e, w
    The value is going to be a room id as well
    
    This will allow us to index a room and apply a room id to a direction of the current room
    """
    def add_edge(self, vertex, key, value):
        self.vertices[vertex][key] = value
        
        