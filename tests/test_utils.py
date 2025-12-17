import pytest
from chatlan.utils import format_msg,unformat_msg

@pytest.mark.parametrize("input_value, expected",
        (
            ("Mobsy Joined The Chat",b"Mobsy Joined The Chat\n"),
            (b"Mobsy Joined The Chat",b"Mobsy Joined The Chat\n"),
            ("Mobsy: Hi guys\n\t",b"Mobsy: Hi guys\n\t\n"),
            ("",b"\n"),
            (b"",b"\n")
        ))
def test_format_msg(input_value,expected):
    assert format_msg(input_value) == expected
    
@pytest.mark.parametrize("input_value, expected",
                         (
                             ("Mobsy Joined The Chat\n","Mobsy Joined The Chat"),
                             (b"Mobsy Joined The Chat\n","Mobsy Joined The Chat"),
                             ("Mobsy: Hi Guys\n","Mobsy: Hi Guys"),
                             ("Mobsy: Hi Guys\n\t\t","Mobsy: Hi Guys\n\t"),
                             ("Mobsy: Hi Guys","Mobsy: Hi Guy"),
                             ("",""),
                             (b"","")
                         ))
def test_unformat_msg(input_value, expected):
    assert unformat_msg(input_value) == expected