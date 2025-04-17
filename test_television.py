import pytest
from television import *

class TestTelevision:
    """
    A class that tests functionality of Television class
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3


    def test_init(self):
        """Test that __init__ sets correct initial values"""
        tv = Television()
        assert str(tv) == "Power = [False], Channel = [0], Volume = [0]"


    def test_power(self):
        """Test the power toggling on/off"""
        tv = Television()

        # Television ON
        tv.power()
        assert "Power = [True]" in str(tv)

        # Television OFF
        tv.power()
        assert "Power = [False]" in str(tv)


    def test_mute(self):
        """Test the mute functionality."""
        tv = Television()

        # Television ON
        tv.power()

        # Mute the TV
        tv.mute()
        assert tv._Television__muted is True

        # Unmute the TV
        tv.mute()
        assert tv._Television__muted is False

        # Test no mute functionality with TV OFF
        tv.power() # TV OFF
        tv.mute()
        assert tv._Television__muted is False


    def test_channel_up(self):
        """Test no channel change when TV OFF"""
        tv = Television()

        # Test no channel functionality when TV OFF
        init_channel = tv._Television__channel
        tv.channel_up()
        assert tv._Television__channel == init_channel

        # TV ON
        tv.power()

        # Test channel up with TV ON
        init_channel = tv._Television__channel
        tv.channel_up()
        assert tv._Television__channel == init_channel + 1

        # Channel wraps around at max
        tv._Television__channel = Television.MAX_CHANNEL
        tv.channel_up()
        assert tv._Television__channel == Television.MIN_CHANNEL


    def test_channel_down(self):
        """Test channel_down functionality"""
        tv = Television()

        # Test no channel functionality when TV OFF
        init_channel = tv._Television__channel
        tv.channel_down()
        assert tv._Television__channel == init_channel

        # TV ON
        tv.power()

        # Test channel down with TV ON
        tv._Television__channel = 1
        tv.channel_down()
        assert tv._Television__channel == 0

        # Channel wraps around at min
        tv._Television__channel = Television.MIN_CHANNEL
        tv.channel_down()
        assert tv._Television__channel == Television.MAX_CHANNEL


    def test_volume_up(self):
        """Test volume_up functionality"""
        tv = Television()

        # Test that volume doesn't change with TV OFF
        initial_volume = tv._Television__volume
        tv.volume_up()
        assert tv._Television__volume == initial_volume

        # TV ON
        tv.power()

        # Test normal volume function
        initial_volume = tv._Television__volume
        tv.volume_up()
        assert tv._Television__volume == initial_volume + 1

        # Test max volume
        tv._Television__volume = Television.MAX_VOLUME
        tv.volume_up()
        assert tv._Television__volume == Television.MAX_VOLUME

        # Test volume up breaks mute status
        tv._Television__muted = True
        tv.volume_up()
        assert tv._Television__muted is False


    def test_volume_down(self):
        """Test volume_down functionality"""
        tv = Television()

        # Test no volume changes when TV OFF
        init_volume = tv._Television__volume
        tv.volume_down()
        assert tv._Television__volume == init_volume

        # TV ON
        tv.power()

        # Test min volume change
        tv._Television__volume = Television.MIN_VOLUME
        tv.volume_down()
        assert tv._Television__volume == Television.MIN_VOLUME

        # Test normal volume down
        tv._Television__volume = 2
        tv.volume_down()
        assert tv._Television__volume == 1

        # Test volume down breaks mute status
        tv._Television__muted = True
        tv.volume_down()
        assert tv._Television__muted is False
