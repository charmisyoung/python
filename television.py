class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3


    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.__MIN_VOLUME
        self.__channel = self.__MIN_CHANNEL


    def power(self):
        self.__status = not self.__status


    def mute(self):
        if not self.__status:
            return
        self.__muted = not self.__muted


    def channel_up(self):
        if not self.__status:
            return

        if self.__channel == self.__MAX_CHANNEL:
                self.__channel = self.__MIN_CHANNEL
        else:
            self.__channel += 1


    def channel_down(self):
        if not self.__status:
            return

        if self.__channel == self.__MIN_CHANNEL:
            self.__channel = self.__MAX_CHANNEL
        else:
            self.__channel -= 1


    def volume_up(self):
        if not self.__status:
            return

        if self.__muted:
            self.__muted = False

        if self.__volume < self.__MAX_VOLUME:
            self.__volume += 1


    def volume_down(self):
        if not self.__status:
            return

        if self.__muted:
            self.__muted = False

        if self.__volume > self.__MIN_VOLUME:
            self.__volume -= 1


    def __str__(self):
        if self.__muted:
            return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [0]"
        else:
            return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}]"
