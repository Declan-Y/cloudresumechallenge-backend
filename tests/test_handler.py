from src import main
import pytest

def test_increment():
    current = 0
    current = main.increment_count(current)
    assert(current == 1)
