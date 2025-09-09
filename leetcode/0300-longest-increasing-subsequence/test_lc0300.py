import importlib.util
from pathlib import Path

# Load the solution.py that sits next to this test
sol_path = Path(__file__).parent / "solution.py"
spec = importlib.util.spec_from_file_location("solution", sol_path)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)


def test_basic():
    assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert solution.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert solution.lengthOfLIS([7, 7, 7, 7]) == 1
    assert solution.lengthOfLIS([1, 2, 3, 4]) == 4
    assert solution.lengthOfLIS([5, 4, 3, 2, 1]) == 1
