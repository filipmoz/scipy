"""Basic scipy stats tests."""
import pytest
from scipy import stats
import numpy as np


def test_mean_std():
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    assert np.isclose(np.mean(x), 3.0)
    assert np.isclose(np.std(x, ddof=1), np.sqrt(2.5))


def test_ttest_1samp():
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    t, p = stats.ttest_1samp(x, 3.0)
    assert np.isclose(t, 0.0)
    assert np.isclose(p, 1.0)
