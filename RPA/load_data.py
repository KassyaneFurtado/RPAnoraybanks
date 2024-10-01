from pandas import read_csv

from os import getenv

def loadCases():
    return read_csv(getenv('CASES_CSV'))

def loadSamples():
    return read_csv(getenv('SAMPLES_CSV'))

def loadPositions():
    return read_csv(getenv('POSITIONS_CSV'))