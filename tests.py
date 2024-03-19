from look_and_say import solution
import pytest

@pytest.mark.parametrize("n, result, method", [
    (3, "21","recursive"),(4, "21","recursive"),(5, "12","recursive"),(6, "22","recursive"),(7, "12","recursive"),(8, "21","recursive"),
    (3, "21","loop"),(4, "21","loop"),(5, "12","loop"),(6, "22","loop"),(7, "12","loop"),(8, "21","loop"),
])
def test_accuracy(n, result, method):
    assert solution(n, method) == result

@pytest.mark.timeout(5)
@pytest.mark.parametrize("n, result, method", [
    (100, "**", "recursive"), (100, "**", "loop")
])
def test_efficiency_loop(n, result, method):
    assert solution(n, method) == result
