class Room:
    def __init__(self, room_number, id=None):
        self.room_number = room_number
        self.id = id
        self.remaining_capacity = 1

    def capacity_change_in(self):
        self.remaining_capacity -= 1

    def capacity_change_out(self):
        self.remaining_capacity += 1