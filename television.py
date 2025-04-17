class Television:
    """
    A class that carries the basic functions of a television set.

    Class variables:
    MIN_VOLUME: The lowest setting possible for volume level.
    MAX_VOLUME: The highest setting possible for volume level.
    MIN_CHANNEL: The lowest-numbered channel available.
    MAX_CHANNEL = The highest-numbered channel available.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3


    def __init__(self) -> None:
        """
        Method to set default values of the television.
        :param status: Indicates whether the television is on or off.
        :param muted: Indicates whether the television is muted or un-muted (no volume or previously set volume)
        :param volume: Indicates/sets the volume level of the television
        :param channel: Indicates/sets the channel value that the television is set to
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL


    def power(self) -> None:
        """
        Method to toggle power to television on/off.
        """
        self.__status = not self.__status


    def mute(self) -> None:
        """
        Method to toggle mute function of television (if powered on).
        """
        if not self.__status:
            return
        self.__muted = not self.__muted


    def channel_up(self) -> None:
        """
        Method to increment television channel by 1 (if powered on),
        and if already at maximum channel, cycle back through minimum.
        """
        if not self.__status:
            return

        if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1


    def channel_down(self) -> None:
        """
        Method to decrement television channel by 1 (if powered on),
        and if already at minimum channel, cycle through maximum channel.
        """
        if not self.__status:
            return

        if self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1


    def volume_up(self) -> None:
        """
        Method to increase television volume by 1 (if powered on).
        If the television is muted, this will un-mute the television.
        If the television is at maximum volume, volume remains unchanged.
        """
        if not self.__status:
            return

        if self.__muted:
            self.__muted = False

        if self.__volume < self.MAX_VOLUME:
            self.__volume += 1


    def volume_down(self) -> None:
        """
        Method to decrease television volume by 1 (if powered on).
        If the television is muted, this will un-mute the television.
        If the television is at minimum volume, volume remains unchanged.
        """
        if not self.__status:
            return

        if self.__muted:
            self.__muted = False

        if self.__volume > self.MIN_VOLUME:
            self.__volume -= 1


    def __str__(self) -> str:
        """
        :return: string of the current status of the television's settings.
        If muted, show volume 0.
        """
        if self.__muted:
            return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [0]"
        else:
            return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}]"
