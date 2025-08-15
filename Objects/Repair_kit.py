from GameFrame import RoomObject, Globals
from GameFrame import Globals

class Repair_kit(RoomObject):
    
    def __init__(self,room,x,y):
        RoomObject.__init__(self,room,x,y)
        image = self.load_image("Repair_kit.png")
        self.set_image(image,42,42)
        self.set_direction(180, 5)
        self.register_collision_object("Ship")
        
    def step(self):
        self.outside_of_room()
    
    def handle_collision(self, other, other_type):
        # ship collision
        if other_type == "Ship":
            self.room.astronaut_saved.play()
            self.room.delete_object(self)
            Globals.LIVES += 1
            self.room.lives.update_image()
            
    def outside_of_room(self):
        if self.x + self.width < 0:
            self.room.delete_object(self)