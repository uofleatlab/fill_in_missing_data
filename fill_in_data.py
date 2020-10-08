# iterative imputation transform for the horse colic dataset
from numpy import isnan
from pandas import read_csv
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import pandas as pd
import statsmodels.imputation.mice as mice
import statsmodels.api as sm

## reads the datafile and saves it as a dataframe
missingData = pd.read_csv('')

# load dataset
dataframe = missingData

# split into input and output elements
data = dataframe.values

imputer = IterativeImputer()

# fit on the dataset
imputer.fit(missingData)

# transform the dataset
Xtrans = imputer.transform(missingData)

# print total missing
print('Missing: %d' % sum(isnan(Xtrans).flatten()))


pd.DataFrame(Xtrans.round()).to_csv('')
