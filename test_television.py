import pytest
from television import *

class Test:
    """
    A class that tests functionality of Television class
    """
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        """Test that __init__ sets correct initial values"""
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'


    def test_power(self):
        """Test the power toggling on/off"""

        # TV power ON
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # TV power OFF
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'


    def test_mute(self):
        """Test the mute functionality."""
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()    # TV ON

        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.power()
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 1'

        self.tv1.mute()     # Attempt to unmute, TV OFF
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 1'


    def test_channel_up(self):
        """Test no channel change when TV OFF"""
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 1, Volume = 0'

        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'


    def test_channel_down(self):
        """Test channel_down functionality"""
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()    # TV ON
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 3, Volume = 0'   # TV cycles back to channel 3 past min


    def test_volume_up(self):
        """Test volume_up functionality"""
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()    # TV ON
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.mute()     # Mute the TV
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'


    def test_volume_down(self):
        """Test volume_down functionality"""
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()    # TV ON
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

        self.tv1.mute()     # Mute the TV
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'