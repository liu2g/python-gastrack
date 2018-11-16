# Author      : Zuguang Liu
# Date        : 2018-11-15 18:52:07
# Python Ver  : 3.6
# Description : 

import pandas as pd
import numpy as np

df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo","bar", "bar", "bar", "bar"],"B": ["one", "one", "one", "two", "two","one", "one", "two", "two"],"C": ["small", "large", "large", "small","small", "large", "small", "small","large"],"D": [1, 2, 2, 3, 3, 4, 5, 6, 7]})

table = pd.pivot_table(df, columns=['A'], aggfunc=[max,min,np.mean])
print(table)