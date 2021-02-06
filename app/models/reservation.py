class Reservation:
    def __init__(self, guest, room, arrival_date, departure_date, id=None):
        self.guest = guest
        self.room = room
        self.arrival_date = arrival_date
        self.departure_date = departure_date
        self.status = "Incoming"
        self.id = id

    def status_change(self):
        if self.status == "Incoming":
            self.status == "Checked In"
        elif self.status == "Checked In":
            self.status == "Departed"
        else:
            return "Status Error"