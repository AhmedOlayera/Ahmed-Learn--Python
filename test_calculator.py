import subprocess
import sys


def test_addition():
    result = subprocess.run(
        [sys.executable, "calculator.py", "5", "+", "10"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "15.0"


def test_division_by_zero():
    result = subprocess.run(
        [sys.executable, "calculator.py", "10", "/", "0"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 1
    assert "Cannot divide by zero" in result.stderr