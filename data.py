import pandas as pd
from WindPy import *
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Line, Scatter, Page, Grid, Bar,Pie
import numpy as np

from DataProcessing import plot_line_from_wind,plot_mutiple_line_from_wind,plot_mutiple_line_not_from_wind,plot_line_not_from_wind
import datetime as dt

from PlotFunction import plot_line,plot_pie
from GetDataFromWind import get_data_from_wind,get_data_from_wind_mutiple_same_date

w.start()

enddate = dt.datetime.now().date().strftime("%Y-%m-%d") # 截至今日

china_pork_price_line = plot_line_from_wind("S5914495","外三元生猪市场价","pork_price","1990-07-01",enddate)
pork_price_22_city_line = plot_line_from_wind("S0113892","22省市猪肉平均价","pork_price_22_city","1990-07-01",enddate)
china_pork_import_line = plot_line_from_wind("S5011199","中国猪肉进口量","china_pork_import","1990-07-01",enddate)

china_breading_sows_line = plot_line_from_wind("S0114187","中国能繁母猪存栏量","china_breeding_sows_number","1975-01-01",
                                               enddate)

china_pork_number_line = plot_line_from_wind("S0114186","中国生猪存栏量","china_pork_number","1975-01-01",enddate)

china_pork_consume_line = plot_line_from_wind("S5011196","中国猪肉消费量（年）","china_pork_consume","1975-01-01",
                                              enddate)
china_pork_produce_line = plot_line_from_wind("S5011200","中国猪肉产量（年）","china_pork_produce","1975-01-01",
                                              enddate)

china_pork_corn_line = plot_line_from_wind("S0113895","猪粮比","pork_corn_ratio","1975-01-01",enddate)
china_pork_feed_line = plot_line_from_wind("S5021737","猪料比","pork_feed_ratio","1975-01-01",enddate)


# 需要补充MSY（每年每头母猪出栏肥猪头数）

china_pork_consumption_per_capita_urban_resident_id = "M6178362"
china_pork_consumption_per_capita_rural_resident_id = "M6178847"
china_pork_consumption_per_capita_id = "M6177877"

china_pork_consumption_list = [china_pork_consumption_per_capita_id,
                               china_pork_consumption_per_capita_rural_resident_id,
                               china_pork_consumption_per_capita_urban_resident_id]

china_pork_consumption_per_capita_df = get_data_from_wind_mutiple_same_date(china_pork_consumption_list,
                                                                            "2013-01-01", enddate,
                                                                            ["total", "rural", "urban"]).round(decimals=2)

china_pork_consumption_per_capita_tuple = [i[0] for i in china_pork_consumption_per_capita_df.total.values]
china_pork_consumption_per_capita_rural_tuple = [i[0] for i in china_pork_consumption_per_capita_df.rural.values]
china_pork_consumption_per_capita_urban_tuple = [i[0] for i in china_pork_consumption_per_capita_df.urban.values]
china_pork_consumption_per_capita_date = [i[0] for i in china_pork_consumption_per_capita_df.Date.values]

barx = (
    Bar()

)

china_pork_per_capita_bar = (
    Bar()
    .add_xaxis(china_pork_consumption_per_capita_date)
    .add_yaxis("全国人均消费量", china_pork_consumption_per_capita_tuple)
    .add_yaxis("城镇人均消费量", china_pork_consumption_per_capita_urban_tuple)
    .add_yaxis("农村人均消费量", china_pork_consumption_per_capita_rural_tuple)
    .set_global_opts(
        title_opts=opts.TitleOpts(title = "人均猪肉消费量"),
        toolbox_opts= opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=True)) # 用于控制图例
)


df_world_pork_import = pd.read_excel(u"D:\商品\生猪\Pork_Trade_Data_USDA.xlsx",sheet_name="Total Import")
df_world_pork_import["Total Imports"]=df_world_pork_import["Total Imports"].str.strip()
df_world_pork_import = df_world_pork_import[df_world_pork_import["Total Imports"] != "Total"]
df_world_pork_import = df_world_pork_import[df_world_pork_import["Total Imports"] != "Total Foreign"]
df_world_pork_import[2018].apply(lambda x: int(x))
data_pair = [list(z) for z in zip(df_world_pork_import["Total Imports"].values, [int(i) for i in df_world_pork_import[2018]])]
world_pork_import_pie = plot_pie(data_pair,"全球猪肉进口","")


df_world_pork_export = pd.read_excel(u"D:\商品\生猪\Pork_Trade_Data_USDA.xlsx",sheet_name="Total Export")
df_world_pork_export["Total Exports"] = df_world_pork_export["Total Exports"].str.strip()
df_world_pork_export = df_world_pork_export[df_world_pork_export["Total Exports"] != "Total"]
df_world_pork_export = df_world_pork_export[df_world_pork_export["Total Exports"] != "Total Foreign"]
df_world_pork_export[2018].apply(lambda x:int(x))
data_pair_export = [list(z) for z in zip(df_world_pork_export["Total Exports"].values,[int(i) for i in df_world_pork_export[2018]])]
world_pork_export_pie = plot_pie(data_pair_export,"全球猪肉出口","")




## 债券市场

line_liquidity_watch = plot_mutiple_line_from_wind(["M1006337", "M1001795" ,"M1001858"],"流动性溢价",["DR007","R007","Shibor3M"],"2018-01-01",enddate)
df_liquidity_medium = get_data_from_wind_mutiple_same_date(["M1001858","M1001855"], "2006-01-01",enddate,["Shibor3M","Shibor1W"])
#df_liquidity_medium = plot_mutiple_line_from_wind(["M1001858","M1001855"],"中期流动性观察",["Shibor3M","Shibor1W"],"2006-01-01","2019-09-29")

## 因为column名称不同，所以需要使用values
df_liquidity_medium["Shibor3M - Shibor1W"] = (df_liquidity_medium["Shibor3M"] - df_liquidity_medium["Shibor1W"].values).round(2)
line_liquidity_medium_watch = plot_mutiple_line_not_from_wind(df_liquidity_medium,"中期流动性观察",["Shibor3M","Shibor1W"],"Shibor3M - Shibor1W",1,True)


df_liquidity_expectation = get_data_from_wind_mutiple_same_date(["M0048486","M1006337"], "2014-01-01",enddate,["FR0071YIRS","DR007"])
df_liquidity_expectation["FR0071YIRS - DR007"] = (df_liquidity_expectation["FR0071YIRS"] - df_liquidity_expectation["DR007"].values).round(2)
line_liquidity_expectation = plot_line_not_from_wind(df_liquidity_expectation,"流动性预期","FR0071YIRS - DR007")


df_china_bond =get_data_from_wind_mutiple_same_date(["M1000166","M1000164","M1000162","M1000158"], "2010-01-01",enddate,["10Y","7Y","5Y","1Y"])
df_china_bond["10Y - 1Y"] = (df_china_bond["10Y"] - df_china_bond["1Y"].values).round(2)
df_china_bond["5Y - 1Y"] = (df_china_bond["5Y"] - df_china_bond["1Y"].values).round(2)
df_china_bond["10Y - 5Y"] = (df_china_bond["10Y"] - df_china_bond["5Y"].values).round(2)


line_china_treasury = plot_mutiple_line_from_wind(["M1000166","M1000164","M1000162","M1000158"],"国债收益率",["10Y","7Y","5Y","1Y"],"2010-01-01",enddate)
line_term_spread = plot_mutiple_line_not_from_wind(df_china_bond[["Date","10Y - 1Y","10Y - 5Y","5Y - 1Y"]],"期限利差",["10Y - 1Y","10Y - 5Y","5Y - 1Y"],0,0,0)

windidStr = ["M1004306","M1004304","M1004302","M1004300","M1004298","M1000166","M1000164","M1000162","M1000160","M1000158"]
treasury_localgov = ["10Y_local","7Y_local","5Y_local","3Y_local","1Y_local","10Y_treasury","7Y_treasury","5Y_treasury","3Y_treasury","1Y_treasury"]


df_china_treasury_localgov_spread = get_data_from_wind_mutiple_same_date(windidStr,"2011-01-01",enddate,treasury_localgov)

df_china_treasury_localgov_spread["10Y spread"] = (df_china_treasury_localgov_spread["10Y_local"] - df_china_treasury_localgov_spread["10Y_treasury"].values).round(2)
df_china_treasury_localgov_spread["7Y spread"] = (df_china_treasury_localgov_spread["7Y_local"] - df_china_treasury_localgov_spread["7Y_treasury"].values).round(2)
df_china_treasury_localgov_spread["5Y spread"] = (df_china_treasury_localgov_spread["5Y_local"] - df_china_treasury_localgov_spread["5Y_treasury"].values).round(2)
df_china_treasury_localgov_spread["3Y spread"] = (df_china_treasury_localgov_spread["3Y_local"] - df_china_treasury_localgov_spread["3Y_treasury"].values).round(2)

line_china_treasury_localgov_spread = plot_mutiple_line_not_from_wind(df_china_treasury_localgov_spread[["Date","10Y spread","7Y spread","5Y spread","3Y spread"]],"国债地方债利差",["10Y spread","7Y spread","5Y spread","3Y spread"],0,0,0)

wind_treasury_creditbond_id = ["M1000532","M1000534","M1000536","M1000166","M1000164","M1000162","M1000160","M1000158"]
treasury_creditbond_str = ["AAA短融：1Y","AAA中票：3Y","AAA中票：5Y","10Y_treasury","7Y_treasury","5Y_treasury","3Y_treasury","1Y_treasury"]


df_china_credit_bond = get_data_from_wind_mutiple_same_date(wind_treasury_creditbond_id,"2010-01-01",enddate,treasury_creditbond_str)
df_china_credit_bond["5Y spread"] = (df_china_credit_bond["AAA中票：5Y"] - df_china_credit_bond["5Y_treasury"].values).round(2)
df_china_credit_bond["3Y spread"] = (df_china_credit_bond["AAA中票：3Y"] - df_china_credit_bond["3Y_treasury"].values).round(2)
df_china_credit_bond["1Y spread"] = (df_china_credit_bond["AAA短融：1Y"] - df_china_credit_bond["1Y_treasury"].values).round(2)

line_china_credit_spread_line = plot_mutiple_line_not_from_wind(df_china_credit_bond[["Date","5Y spread","3Y spread","1Y spread"]],"主要期限信用债利差",["5Y spread","3Y spread","1Y spread"],0,0,0)



wind_1Y_treasury_creditbond_id = ["M1000532","M1000571","M1000583","M1000158"]
treasury_creditbond_1Y_str = ["1Y短融AAA","1Y短融AA","1Y短融AA-","1Y treasury"]
df_1Y_credit_treasury_spread = get_data_from_wind_mutiple_same_date(wind_1Y_treasury_creditbond_id,"2010-01-01",enddate,treasury_creditbond_1Y_str)
df_1Y_credit_treasury_spread["1Y短融AAA - 1Y treasury"] = (df_1Y_credit_treasury_spread["1Y短融AAA"] - df_1Y_credit_treasury_spread["1Y treasury"].values).round(2)
df_1Y_credit_treasury_spread["1Y短融AA - 1Y treasury"] = (df_1Y_credit_treasury_spread["1Y短融AA"] - df_1Y_credit_treasury_spread["1Y treasury"].values).round(2)
df_1Y_credit_treasury_spread["1Y短融AA- - 1Y treasury"] = (df_1Y_credit_treasury_spread["1Y短融AA-"] - df_1Y_credit_treasury_spread["1Y treasury"].values).round(2)

line_china_credit_spread_1Y_line = plot_mutiple_line_not_from_wind(df_1Y_credit_treasury_spread[["Date","1Y短融AAA - 1Y treasury","1Y短融AA - 1Y treasury","1Y短融AA- - 1Y treasury"]],
                                                                "主要级别1Y信用利差",["1Y短融AAA - 1Y treasury","1Y短融AA - 1Y treasury","1Y短融AA- - 1Y treasury"],0,0,0)



## Economic Activity

line_china_GDP_NoChange = plot_mutiple_line_from_wind(["M5567889","M5567890","M5567891","M5567892"],"GDP不变价当季值",["GDP","第一产业","第二产业","第三产业"],"2007-01-01",enddate,is_show = False)
line_china_GDP_yoy = plot_mutiple_line_from_wind(["M0039354","M5567901","M5567902","M5567903"],"GDP不变价同比",["GDP","第一产业","第二产业","第三产业"],"1992-01-01",enddate,is_show = False)

line_china_GDP_industry_yoy = plot_mutiple_line_not_from_wind([])


page = (
    Page()
    .add(china_pork_price_line,pork_price_22_city_line,china_pork_corn_line, china_pork_feed_line,china_pork_consume_line,
         china_pork_produce_line, china_pork_import_line,china_pork_per_capita_bar,china_pork_number_line,
         china_breading_sows_line, world_pork_import_pie,world_pork_export_pie,line_liquidity_watch,
         line_liquidity_medium_watch,line_liquidity_expectation,line_china_treasury,line_term_spread,line_china_treasury_localgov_spread,line_china_credit_spread_line,line_china_credit_spread_1Y_line,
         line_china_GDP_NoChange,line_china_GDP_yoy)
)

page.render(enddate + ".html")

