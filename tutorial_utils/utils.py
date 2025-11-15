import os

def data_dir():
    '''
    Returns the path to the 'data' folder
    '''
    return os.path.dirname(os.path.abspath(__file__)) + '/data/'

