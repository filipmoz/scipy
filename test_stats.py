"""Basic scipy stats tests."""
import numpy as np
import pytest
from scipy import stats


def test_mean_std():
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    assert np.isclose(np.mean(x), 3.0)
    assert np.isclose(np.std(x, ddof=1), 1.581128874, rtol=1e-5)


def test_median():
    x = np.array([1.0, 3.0, 2.0, 5.0, 4.0])
    assert np.isclose(np.median(x), 3.0)


def test_ttest_1samp():
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    t, p = stats.ttest_1samp(x, 3.0)
    assert np.isclose(t, 0.0)
    assert np.isclose(p, 1.0)


def test_normaltest():
    rng = np.random.default_rng(42)
    x = rng.normal(0, 1, 100)
    stat, p = stats.normaltest(x)
    assert p > 0.05


def test_pearsonr():
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    y = np.array([2.0, 4.0, 6.0, 8.0, 10.0])
    r, p = stats.pearsonr(x, y)
    assert np.isclose(r, 1.0)
    assert np.isclose(p, 0.0)
