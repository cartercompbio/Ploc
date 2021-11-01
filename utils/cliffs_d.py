import numpy as np
def calc_boxplot_effect_size(n_a, n_b, U):
    '''Cliffs D
    - n_a = number in category A
    - n_b = number in category B
    - U statistic from MW test
    '''
    return np.abs(((2*U)/(n_a*n_b))-1)
