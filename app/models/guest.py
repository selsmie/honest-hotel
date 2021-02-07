class Guest:
    def __init__(self, name, stays, id=None):
        self.name = name
        self.id = id
        self.stays = stays

    def increase_stay_count(self):
        self.stays += 1 
