import pandas as pd

from PlotFunction import *
from GetDataFromWind import *


def plot_line_from_wind(wind_id, name_str, var_name, start_date, end_date):
    _df = get_data_from_wind(wind_id, start_date, end_date, ["Date", var_name])
    _date_tuple = [i[0] for i in _df.Date.values]
    _data_tuple = [i[0] for i in _df[var_name].values]

    _line = plot_line(_date_tuple, _data_tuple, name_str, "{value}")
    return _line


def plot_line_not_from_wind(df,name_str,var_name):
    _date_tuple = [i[0] for i in df.Date.values]
    _data_tuple = [i[0] for i in df[var_name].values]

    _line = plot_line(_date_tuple, _data_tuple, name_str, "{value}")
    return _line


def plot_mutiple_line_from_wind(wind_id, name_str, var_name, start_date, end_date):
    _df = get_data_from_wind_mutiple_same_date(wind_id, start_date, end_date, var_name)
    _date_tuple = [i[0] for i in _df.Date.values]
    _data_tuple_dict = dict()
    for _name in var_name:
        _data_tuple_dict[_name] = [i[0] for i in _df[_name].values]
    _line = plot_multiple_line(_date_tuple, _data_tuple_dict, name_str, 0, double_ylabel=False)

    return _line


def plot_mutiple_line_not_from_wind(_df,name_str, var_name,var_name_y_label,double_ylabel,ylabel_smooth):
    _date_tuple = [i[0] for i in _df.Date.values]
    _data_tuple_dict = dict()
    total_name = []
    total_name = var_name.copy()
    if double_ylabel:
        total_name.append(var_name_y_label)
    for _name in total_name:
        _data_tuple_dict[_name] = [i[0] for i in _df[_name].values]
    _line = plot_multiple_line(_date_tuple, _data_tuple_dict, name_str, var_name_y_label, double_ylabel,ylabel_smooth= ylabel_smooth)

    return _line