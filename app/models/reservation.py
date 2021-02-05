class Reservation:
    def __init__(self, guest, room, id=None):
        self.guest = guest
        self.room = room
        self.id = id