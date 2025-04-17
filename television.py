class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3


    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL


    def power(self):
        self.status = not self.status


    def mute(self):
        if not self.status:
            return
        self.muted = not self.muted


    def channel_up(self):
        if not self.status:
            return

        if self.channel == self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL
        else:
            self.channel += 1


    def channel_down(self):
        if not self.status:
            return

        if self.status:
            if self.channel == self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL
            else:
                self.channel -= 1


    def volume_up(self):
        if not self.status:
            return

        if self.muted:
            self.muted = False

        if self.volume < self.MAX_VOLUME:
            self.volume += 1


    def volume_down(self):
        if not self.status:
            return

        if self.muted:
            self.muted = False

        if self.volume > self.MIN_VOLUME:
            self.volume -= 1


    def __str__(self):
        if self.muted:
            return f"Power = [{self.status}], Channel = [{self.channel}], Volume = [0]"
        else:
            return f"Power = [{self.status}], Channel = [{self.channel}], Volume = [{self.volume}]"
