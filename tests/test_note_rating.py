from src.note_rating import rate_note
import pytest

@pytest.mark.parametrize("note",[7,8,9])
def test_rate_note_unsuccessful(note):
    assert rate_note(note) == "unsuccessful"

def test_rate_10_returns_acceptable():
            assert rate_note(10) == "acceptable"
