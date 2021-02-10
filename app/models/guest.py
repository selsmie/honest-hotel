class Guest:
    def __init__(self, name, stays=0, preferences="", id=None):
        self.name = name
        self.id = id
        self.stays = stays
        self.preferences = preferences

    def increase_stay_count(self):
        self.stays += 1 
