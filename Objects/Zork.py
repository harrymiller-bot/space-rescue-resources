from GameFrame import RoomObject, Globals
from Objects.Asteroid import Asteroid
from Objects.Astronaut import Astronaut
from Objects.Repair_kit import Repair_kit
import random

class Zork(RoomObject):
    """
    A class for the game's antagoist
    """
    def __init__(self, room, x, y):
        """
        Initialise the Boss object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Zork.png")
        self.set_image(image,135,165)
        
        # set inital movement
        self.y_speed = random.choice([-10, 10])
        
        # start asteroid timer
        asteroid_spawn_time = random.randint(15, 150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)
        
        # start astronaut timer
        astronaut_spawn_time = random.randint(30, 200)
        self.set_timer(astronaut_spawn_time, self.spawn_astronaut)
        
        repair_kit_spawn_time = random.randint(1, 300)
        self.set_timer(repair_kit_spawn_time, self.spawn_repair_kit)

        
    def keep_in_room(self):
        """
        Keeps the Zork inside the top and bottom room limits
        """
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
            
    def step(self):
        """
        Determine what happens to the Dragon on each tick of the game clock
        """
        self.keep_in_room()
        
    def spawn_asteroid(self):
        """
        Randomly spawns a new Asteroid
        """
        # spawn Asteroid and add to room
        new_asteroid = Asteroid(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_asteroid)
        
        # reset time for next Asteroid spawn
        asteroid_spawn_time = random.randint(15, 150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)
        
    def spawn_astronaut(self):
        """
        Randomly spawns a new astronaut
        """
        # spawn astronaut and add to room
        new_astronaut = Astronaut(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_astronaut)
        
        # reset timer for next astronaut spawn
        astronaut_spawn_time = random.randint(30, 200)
        self.set_timer(astronaut_spawn_time, self.spawn_astronaut)

    def spawn_repair_kit(self):
        # spawn repair kit and add to room
        new_repair_kit = Repair_kit(self.room, self.x, self.y)
        self.room.add_room_object(new_repair_kit)
        
        # reset timer for next repair kit spawn
        repair_kit_spawn_time = random.randint(1, 500)
        self.set_timer(repair_kit_spawn_time, self.spawn_repair_kit)
        print("Spawned repair kit")  # Debugging message