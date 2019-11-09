import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Line, Scatter, Page, Grid, Bar, Pie


def plot_line(x_axis, y_axis, title, label_format):
    line = (
        Line()
        .add_xaxis(x_axis)
        .add_yaxis(title, y_axis)
        .extend_axis(
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter=label_format), interval=5
            )

        )
        .set_global_opts(title_opts=opts.TitleOpts(title=title),
                         toolbox_opts=opts.ToolboxOpts())

    )
    return line


def plot_pie(data_pair, title, label_format):
    pie = (
        Pie()
        .add(title, data_pair)
        .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(pos_top=20),
            legend_opts=opts.LegendOpts(is_show=True))
    )
    return pie


def plot_multiple_line(x_axis, y_axis_dict, title, double_ylabel_str,double_ylabel = False,ylabel_smooth = False):
    line = Line()
    line.add_xaxis(x_axis)
    for _name in y_axis_dict.keys():
        if _name != double_ylabel_str:
            line.add_yaxis(_name,y_axis_dict[_name])
    line.set_global_opts(title_opts=opts.TitleOpts(title=title), toolbox_opts=opts.ToolboxOpts())
    if double_ylabel:
        line.extend_axis(yaxis= opts.AxisOpts(name = double_ylabel_str,
                                              axislabel_opts=opts.LabelOpts(interval=5)))
        line.add_yaxis(double_ylabel_str,y_axis_dict[double_ylabel_str], yaxis_index=1,is_smooth= ylabel_smooth)

    return line