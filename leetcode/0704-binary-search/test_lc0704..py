import importlib.util
from pathlib import Path

sol_path = Path(__file__).parent / "solution.py"
spec = importlib.util.spec_from_file_location("solution", sol_path)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)


def test_basic():
    assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert solution.search([5], 5) == 0
    assert solution.search([5], -5) == -1
