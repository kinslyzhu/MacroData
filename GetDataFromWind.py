import pandas as pd
import numpy as np
from WindPy import *


def get_data_from_wind(wind_id, start_date, end_date, column_str):
    data = w.edb(wind_id, start_date, end_date)
    data_df = pd.DataFrame(np.transpose([data.Times, data.Data[0]]),
                           index=None,
                           columns=[column_str])
    return data_df

# pork_corn_ratio = "S0113895"
# data = w.edb(pork_corn_ratio, "2009-01-01", "2019-09-14")
# pork_corn_ratio_df = pd.DataFrame(np.transpose([data.Times, data.Data[0]]),
#                                   index=None,
#                                   columns=[["Date", "pork_corn_ratio"]])
def get_data_from_wind_mutiple_same_date(wind_id, start_date, end_date, column_str):
    data = w.edb(wind_id, start_date, end_date)
    data_df = pd.DataFrame(np.transpose(data.Data),
                           index=None,
                           columns=[column_str])
    data_df["Date"] = data.Times

    return data_df