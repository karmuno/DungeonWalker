import random
from .elements import Room, Hallway

class DungeonAgent:
    def __init__(self):
        self.rooms = []
        self.hallways = []
        self.current_position = (0, 0)
        self.room_id = 1

    def generate(self, steps=10):
        self._place_room(self.current_position)

        for _ in range(steps):
            direction = random.choice(["N", "S", "E", "W"])
            new_position = self._move(self.current_position, direction)
            if not self._room_exists(new_position):
                self._place_room(new_position)
                self.hallways.append(Hallway(
                    from_room=self.room_id - 1,
                    to_room=self.room_id,
                    direction=direction,
                    length=1
                ))
                self.current_position = new_position

        return self.rooms, self.hallways

    def _move(self, pos, direction):
        x, y = pos
        return {
            "N": (x, y + 1),
            "S": (x, y - 1),
            "E": (x + 1, y),
            "W": (x - 1, y)
        }[direction]

    def _room_exists(self, pos):
        return any(r.position == pos for r in self.rooms)

    def _place_room(self, pos):
        room = Room(id=self.room_id, position=pos, size=(random.randint(3,6), random.randint(3,6)), doors=[])
        self.rooms.append(room)
        self.room_id += 1
