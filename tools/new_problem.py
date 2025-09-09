#!/usr/bin/env python3
import os
import re
import sys


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


TEMPLATE_README = """# {id}. {title}

- Pattern: {pattern}
- Difficulty: {difficulty}
- Notes:
"""

TEMPLATE_PY = '''"""
{pid} - {title}
"""
from typing import *

# Add your implementation here
'''

# NOTE: double braces {{ }} so .format() doesn't treat them as placeholders
TEMPLATE_CPP = r"""// {pid} - {title}
#include <bits/stdc++.h>
using namespace std;

int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // TODO
    return 0;
}}
"""

TEMPLATE_TEST = """import importlib.util
from pathlib import Path
sol_path = Path(__file__).parent / "solution.py"
spec = importlib.util.spec_from_file_location("solution", sol_path)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_placeholder():
    assert True
"""


def main():
    if len(sys.argv) < 3:
        print("Usage: new_problem.py <id> <title words...>")
        sys.exit(1)
    pid = sys.argv[1]
    title = " ".join(sys.argv[2:])
    folder = f"leetcode/{pid.zfill(4)}-{slugify(title)}"
    os.makedirs(folder, exist_ok=True)

    with open(f"{folder}/README.md", "w") as f:
        f.write(TEMPLATE_README.format(id=pid, title=title, pattern="TBD", difficulty="TBD"))
    with open(f"{folder}/solution.py", "w") as f:
        f.write(TEMPLATE_PY.format(pid=pid, title=title))
    with open(f"{folder}/solution.cpp", "w") as f:
        f.write(TEMPLATE_CPP.format(pid=pid, title=title))
    with open(f"{folder}/test_solution.py", "w") as f:
        f.write(TEMPLATE_TEST)
    print(f"Created {folder}")


if __name__ == "__main__":
    main()
