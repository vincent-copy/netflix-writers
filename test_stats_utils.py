from stats_utils import z_score
import pytest

def test_z_score_basic():
    assert z_score(10, 5, 2) == 2.5

def test_z_score_zero_mean():
    assert z_score(0, 0, 1) == 0.0

def test_z_score_raises_on_zero_std():
    with pytest.raises(ValueError):
        z_score(10, 5, 0)
