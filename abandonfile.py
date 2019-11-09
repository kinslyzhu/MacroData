# line1 = (
#     Line()
#     .add_xaxis(pork_corn_ratio_date)
#     .add_yaxis("猪粮比", pork_corn_ratio_tuple)
#     # .add_yaxis("月度同比",pork_corn_ratio_week_on_week_tuple)
#     .extend_axis(
#     yaxis=opts.AxisOpts(
#         axislabel_opts=opts.LabelOpts(formatter="{value}%"), interval=5
#     )
#     )
#     .set_global_opts(title_opts=opts.TitleOpts(title="猪粮比"))
#
# )



#porkpriceStr = "外三元生猪市场价"
#pork_price_id = "S5914495"
#pork_price_df = get_data_from_wind(pork_price_id, "2009-01-01", "2019-09-14", ["Date", "pork_price"])

#porkprice22cityStr = "22省市猪肉平均价"
#pork_price_22_city_id = "S0113892"
#pork_price_22_city_df = get_data_from_wind(pork_price_22_city_id,"2006-01-01", "2019-09-14", ["Date", "pork_price_22_city"])

china_breading_sows_line = plot_line(china_breading_sows_date,china_breading_sows_tuple,"中国能繁母猪存栏量","{value}")
chinabreedingsowsStr = "中国能繁母猪存栏量"
china_breeding_sows_id = "S0114187"
china_breeding_sows_df = get_data_from_wind(china_breeding_sows_id,"1975-01-01","2019-09-14",
                                            ["Date","china_breeding_sows_number"])



chinaporkimportStr = "中国猪肉进口量"
china_pork_import_id = "S5011199"
china_pork_import_df = get_data_from_wind(china_pork_import_id,"1975-01-01","2019-09-14",["Date","china_pork_import"])


chinaporknumberStr = "中国生猪存栏量"
china_pork_number_id = "S0114186"
china_pork_number_df = get_data_from_wind(china_pork_number_id,"1975-01-01","2019-09-14",["Date","china_pork_number"])
china_pork_number_line = plot_line(china_pork_number_date,china_pork_number_tuple,"中国生猪存栏量","{value}")

china_pork_number_date = [i[0] for i in china_pork_number_df.Date.values]
china_pork_number_tuple = [i[0] for i in china_pork_number_df.china_pork_number.values]


chinaporkconsumeStr = "中国猪肉消费量"
china_pork_consume_id = "S5011196"
china_pork_consume_df = get_data_from_wind(china_pork_consume_id,"1975-01-01","2019-09-14",["Date","china_pork_consume"])

chinaporkproduceStr = "中国猪肉生产量"
china_pork_produce_id = "S5011200"
china_pork_produce_df = get_data_from_wind(china_pork_produce_id,"1975-01-01","2019-09-14",["Date","china_pork_produce"])



china_pork_consume_line = plot_line(china_pork_consume_date, china_pork_consume_tuple,"中国猪肉消费量（年）","{value}")
china_pork_produce_line = plot_line(china_pork_produce_date, china_pork_produce_tuple,"中国猪肉产量（年）","{value}")


china_pork_consume_date = [i[0] for i in china_pork_consume_df.Date.values]
china_pork_consume_tuple = [i[0] for i in china_pork_consume_df.china_pork_consume.values]
china_pork_produce_date = [i[0] for i in china_pork_produce_df.Date.values]
china_pork_produce_tuple = [i[0] for i in china_pork_produce_df.china_pork_produce.values]


#china_breading_sows_date = [i[0] for i in china_breeding_sows_df.Date.values]
#china_breading_sows_tuple = [i[0] for i in china_breeding_sows_df.china_breeding_sows_number.values]

#china_pork_price_date = [i[0] for i in pork_price_df.Date.values]
#china_pork_price_tuple = [i[0] for i in pork_price_df.pork_price.values]

#pork_price_22_city_date = [i[0] for i in pork_price_22_city_df.Date.values]
#pork_price_22_city_tuple = [i[0] for i in pork_price_22_city_df.pork_price_22_city.values]

#china_pork_import_date = [i[0] for i in china_pork_import_df.Date.values]
#china_pork_import_tuple = [i[0] for i in china_pork_import_df.china_pork_import.values]

#china_breading_sows_line = plot_line(china_breading_sows_date,china_breading_sows_tuple,"中国能繁母猪存栏量","{value}")
#china_pork_price_line = plot_line(china_pork_price_date,china_pork_price_tuple,"中国外三元生猪价格","{value}")
#china_pork_import_line = plot_line(china_pork_import_date,china_pork_import_tuple,"中国猪肉进口量（蹲）","{value}")
#pork_price_22_city_line = plot_line(pork_price_22_city_date,pork_price_22_city_tuple,"22省市猪肉价格","{value}")




# scatter1 = (
#     Line()
#         .add_xaxis(pork_corn_ratio_date)
#         # .add_yaxis("猪粮比", pork_corn_ratio_tuple)
#         .add_yaxis("月度同比", pork_corn_ratio_week_on_week_tuple, yaxis_index=1)
#     # .set_global_opts(title_opts=opts.TitleOpts(title=""))
# )
#
# line = (
#     Line()
#         .add_xaxis(pork_corn_ratio_date)
#         .add_yaxis("猪粮比", pork_corn_ratio_tuple)
#         .set_global_opts(title_opts=opts.TitleOpts(title="猪粮比"),
#
#                          )
# )
#
# scatter = (
#     Line()
#         .add_xaxis(pork_corn_ratio_date)
#         # .add_yaxis("猪粮比", pork_corn_ratio_tuple)
#         .add_yaxis("月度同比", pork_corn_ratio_week_on_week_tuple)
#         .set_global_opts(title_opts=opts.TitleOpts(title="月度同比"))
# )

#
# pork_corn_ratio_df["pork_corn_ratio_week_on_week"] = (
#         pork_corn_ratio_df["pork_corn_ratio"].pct_change(periods=4) * 100).round(decimals=2)
# pork_corn_ratio_date = [i[0] for i in pork_corn_ratio_df.Date.values]
# pork_corn_ratio_tuple = [i[0] for i in pork_corn_ratio_df.pork_corn_ratio.values]
# pork_corn_ratio_week_on_week_tuple = [i[0] for i in pork_corn_ratio_df.pork_corn_ratio_week_on_week.values]
#
# pork_feed_ratio_df["pork_feed_ratio_week_on_week"] = (
#         pork_feed_ratio_df["pork_feed_ratio"].pct_change(periods=4) * 100).round(decimals=2)
# pork_feed_ratio_date = [i[0] for i in pork_feed_ratio_df.Date.values]
# pork_feed_ratio_tuple = [i[0] for i in pork_feed_ratio_df.pork_feed_ratio.values]
# pork_feed_ratio_week_on_week_tuple = [i[0] for i in pork_feed_ratio_df.pork_feed_ratio_week_on_week.values]
#
# porkcornStr = "猪粮比"
# pork_corn_ratio_id = "S0113895"
# pork_corn_ratio_df = get_data_from_wind(pork_corn_ratio_id, "2009-01-01", "2019-09-14", ["Date", "pork_corn_ratio"])
#
# porkfeedStr = "猪料比"
# pork_feed_ratio_id = "S5021737"
# pork_feed_ratio_df = get_data_from_wind(pork_feed_ratio_id, "2012-01-01", "2019-09-14", ["Date", "pork_feed_ratio"])



#line1.overlap(scatter1)