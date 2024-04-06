class Breathwork():
    def __init__(self, rounds = 3, totaltime = 10):
        self.rounds = rounds
        self.totaltime = totaltime
        self.time = 0

    def hold(self,time):
        self.time+=time