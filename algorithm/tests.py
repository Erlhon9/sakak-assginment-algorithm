from look_and_say import look_and_say_sequence
import pytest

@pytest.mark.parametrize("n, result", [
    (3, "21"),(4, "21"),(5, "12"),(6, "22"),(7, "12"),(8, "21"),
])
def test_accuracy(n, result):
    assert look_and_say_sequence(n) == result
    
