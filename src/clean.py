'''
import pandas as pd
import numpy as np
import re
'''
def reescribir (i):
    x=str(i)
    x=x.replace('{','  - ')
    x=x.strip('}')
    x=x.replace('\"','')
    x=x.replace(',','\n  - ')
    return(x)