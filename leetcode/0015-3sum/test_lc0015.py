# leetcode/0015-3sum/test_lc0015.py
import importlib.util
from pathlib import Path

# Load the solution.py that sits NEXT to this test file
sol_path = Path(__file__).parent / "solution.py"
spec = importlib.util.spec_from_file_location("solution", sol_path)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)


def test_examples():
    assert sorted(solution.threeSum([-1, 0, 1, 2, -1, -4])) == sorted([[-1, -1, 2], [-1, 0, 1]])
    assert solution.threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert solution.threeSum([1, 2, 3]) == []
    assert solution.threeSum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]
    assert solution.threeSum([100000, -100000, 0]) == [[-100000, 0, 100000]]
