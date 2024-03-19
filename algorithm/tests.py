from look_and_say import solution
import pytest

@pytest.mark.parametrize("n, result", [
    (3, "21"),(4, "21"),(5, "12"),(6, "22"),(7, "12"),(8, "21"),
])
def test_accuracy(n, result):
    assert solution(n) == result
  
@pytest.mark.timeout(5)
@pytest.mark.parametrize("n, result", [
    (100, "**")
])
def test_efficiency(n, result):
    assert solution(n) == result