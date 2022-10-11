

import pandas as pd
import numpy as np

df = pd.read_excel('dblareamethod.xlsx',sheet_name='data')


## need to add the ability to pass column names
def areacalc(df):
    '''
    program reads in x,y cordinates along the perimeter of an area.
    the value returned is the area in the same units (squared) as used in the projected  coordinate system.
    area calc uses a modifyed double maridian distance (DMD) method. modification is for absalute cordinates 
    rather then using difference in departures like traditional DMD method
    '''
    df = pd.concat([df, df.iloc[[0]]]) ## repeats the first value into the last position
    df = df.reset_index(drop = True)    ## fix the index issues caused by concat

    sums = []
    subtrations =[]
    for i in range(len(df)-1):                                  ## without -1 the program will duplicate the last calc for both opperations
        if (i + 1) < len(df):                                   ## prevent diagnal multiplication form running off the end of the table of values
            poducts = df.iat[i, 0] * df.iat[(i+1), 1]           ## downsloping diaganal
            negproducts = df.iat[(i+1), 0] * df.iat[i, 1]       ## upsloping diaganal, values need to be subtracted form downslope 
        sums.append(poducts)
        subtrations.append(negproducts)

    area = np.abs((np.sum(sums) - np.sum(subtrations)) / 2)             ## area is half the sum
    print(area)


if __name__ == '__main__':
    areacalc(df)