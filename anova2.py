#!/usr/bin/python3
from __future__ import print_function

from itertools import combinations

import numpy as np
import scipy.stats as st


def anova_ext(*args, **kwargs):
    """Extended anova algorithm.

    Parameters
    ----------
        arg1, arg2, ..., argn -- samples to be compared;
        transormations -- array of tuples ('trans_name', trans_fun);
                          used to choose appropriate data transformation
        alpha -- level of significance, used when data is checked for normality

    Returns
    -------
        (value of statistic selected,
        p-value,
        statistic's name,
        nonnormal or normal (result of Shapiro-Wilk's test for normality),
        equal or unequal (result of checking for equalness of variances)
        name of transformation used
        )
    """

    def _arcsine_trans(*args):
        maxel = max(map(lambda x: np.max(np.abs(x)), args))
        return map(lambda x: np.arcsin(np.asarray(x) / maxel), args)

    def _log_trans(*args):
        minel = min(map(lambda x: np.min(x), args))
        return map(lambda x: np.log(np.asarray(x) - minel + 1.0), args)

    def _sqrt_trans(*args):
        minel = min(map(lambda x: np.min(x), args))
        return map(lambda x: np.sqrt(np.asarray(x) - minel + 1.0), args)

    def _identity_trans(*args):
        return args

    if 'alpha' not in kwargs:
        alpha = 0.05
    else:
        alpha = kwargs['alpha']
    if 'transformations' not in kwargs:
        transformations = [('identity', _identity_trans),
                           ('arcsine', _arcsine_trans),
                           ('log', _log_trans),
                           ('sqrt', _sqrt_trans)]
    else:
        if 'identity' not in map(lambda x: x[1], transformations):
            transformations = [('identity', lambda x: x)] + kwargs['transformations']
        else:
            transformations = kwargs['transformations']

    def _check_normality(*args):
        for arg in args:
            if st.shapiro(arg)[1] < alpha:
                return False
        return True

    def _check_variance_equality_normal(*args):
        return st.bartlett(*args)[1] > alpha

    def _check_variance_equality_nonnormal(*args):
        return st.levene(*args)[1] > alpha

    dtuple = []
    priorities = []
    for tname, tfun in transformations:
        transformed = tfun(*args)
        if _check_normality(*transformed):
            if _check_variance_equality_normal(*transformed):
                dtuple += [(tname, transformed, 'normal', 'equal')]
                priorities.append(1)
                break
            else:
                if 1 in priorities: break
                dtuple += [('identity', args, 'normal', 'unequal')]
                priorities.append(2)
        else:
            if _check_variance_equality_nonnormal(*transformed):
                if 2 in priorities: break
                dtuple += [(tname, transformed, 'nonnormal', 'equal')]
                priorities.append(3)
            else:
                if 3 in priorities: break
                dtuple += [('identity', args, 'nonnormal', 'unequal')]
                priorities.append(4)
    if 1 in priorities:
        data = dtuple[priorities.index(1)]
        fstat, pval = st.f_oneway(*data[1])
        return fstat, pval, 'fisher', 'normal', 'equal', data[0]
    elif 2 in priorities:
        data = dtuple[priorities.index(2)]
        _pval = 1.0
        _fstat = 0.0
        for a, b in combinations(data[1], 2):
            fstat, pval = st.ttest_ind(a, b, equal_var=False)
            if _pval > pval:
                _pval = pval
                _fstat = fstat
        return _fstat, _pval, 'welch-paired', 'normal', 'unequal', 'identity'
    elif 3 in priorities:
        data = dtuple[priorities.index(3)]
        fstat, pval = st.f_oneway(*data[1])
        return fstat, pval, 'fisher', 'nonnormal', 'equal', data[0]
    elif 4 in priorities:
        data = dtuple[priorities.index(4)]
        fstat, pval = st.kruskal(*data[1])
        return fstat, pval, 'kruskal', 'nonnormal', 'unequal', data[0]


if __name__ == '__main__':
    # three normally distributed samples
    a, b, c = np.random.randn(100), np.random.randn(100), np.random.randn(100)
    print('Applying extended anova scheme to 3 n.d. samples:', anova_ext(a, b, c))

    # We still use Fisher test... dut to its stability
    a, b, c = np.random.rand(200), np.random.rand(100), np.random.rand(300)
    print('Applying extended anova scheme to 3 u.d. samples:', anova_ext(a, b, c))

    # Crazy samples...
    a, b, c = [23, 3, 1, 2, 3, 2, 1], range(1000), np.linspace(20, 30, 100)
    print('Applying extended anova scheme to 3 "crazy" samples:', anova_ext(a, b, c))
