class Servers:

    def __init__(self, server_id, player_id, days):
        self.id = server_id
        self.player = player_id
        self.days = days

    def server_id(self):
        return self.id

    def server_status(self):
        return self.player

    def DDoS(self):
        return self.days 