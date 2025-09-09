import importlib.util
from pathlib import Path

# Load the solution.py that sits NEXT to this test file
sol_path = Path(__file__).parent / "solution.py"
spec = importlib.util.spec_from_file_location("solution", sol_path)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)


def test_placeholder():
    assert True
