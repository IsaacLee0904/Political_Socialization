# Functions
def highlightLoadings(x):
    '''
    highlight the values if they are greater than 0.5 in a Series yellow.
    '''
    return ['background-color: yellow' if abs(v) > 0.5 else '' for v in x]
def highlightCommunalities(x):
    '''
    highlight the values if they are greater than 0.5 in a Series yellow.
    '''
    return ['background-color: yellow' if v > 0.5 else '' for v in x]
def highlightEigenvalue(x):
    '''
    highlight the values if they are greater than 1 in a Series yellow.
    '''
    return ['background-color: yellow' if v > 1 else '' for v in x]