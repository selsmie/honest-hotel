class Room:
    def __init__(self, room_number, id=None):
        self.room_number = room_number
        self.id = id
        self.remaining_capacity = 1