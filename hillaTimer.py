class HillaTimer:
    def __init__(self):
        self.time = 60 * 30
        self.next_time = 29 * 60 + 14

    def decrease_time(self):
        self.time -= 1

    def set_time(self, minutes, seconds):
        self.time = minutes * 60 + seconds

    def check_time_range(self):
        self.decrease_time()
        if self.next_time <= self.time <= self.next_time + 20:
            return True

        return False