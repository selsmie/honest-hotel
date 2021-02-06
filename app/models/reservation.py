class Reservation:
    def __init__(self, guest, room, arrival_date, departure_date, status, id=None):
        self.guest = guest
        self.room = room
        self.arrival_date = arrival_date
        self.departure_date = departure_date
        self.status = status
        self.id = id