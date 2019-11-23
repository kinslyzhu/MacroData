import json

def write_json_to_file(filename,data):
    '''This function is used for writing json file'''
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def read_json_to_python(filename):
    '''This funciton is used for reading json files'''
    txt = open(filename, 'r', encoding='utf8')
    json_txt = json.load(txt)
    return json_txt


def read_json_txt_to_list(json_txt, namestr):
    '''This function return the value need to get from wind'''
    wind_id_list = [k for k in json_txt[namestr]['value'].keys()]
    wind_str_list = [v for v in json_txt[namestr]['value'].values()]
    return json_txt[namestr]["name"], wind_id_list, wind_str_list


def Convert_list_to_pre_json_data(namestr,Wind_id_list,Wind_name_list):
    dict_value_temp = dict(zip(Wind_id_list,Wind_name_list))
    dict_total_temp ={}
    dict_total_temp["name"] = namestr
    dict_total_temp["value"] = dict_value_temp
    return dict_total_temp


Total_data = {}

Wind_id_list = ["M5567904", "M5567905", "M5784264", "M5567906", "M5567907", "M5567908",
        "M5567909", "M5567910", "M5567911", "M5784265", "M5784266", "M5567912",]
Wind_name_list = ["GDP:不变价:农林牧渔业:当季同比", "GDP:不变价:工业:当季同比", "GDP:不变价:工业:制造业:当季同比",
                  "GDP:不变价:建筑业:当季同比", "GDP:不变价:批发和零售业:当季同比", "GDP:不变价:交通运输、仓储和邮政业:当季同比",
                  "GDP:不变价:住宿和餐饮业:当季同比", "GDP:不变价:金融业:当季同比", "GDP:不变价:房地产业:当季同比",
                  "GDP:不变价:信息传输、软件和信息技术服务业:当季同比", "GDP:不变价:租赁和商务服务业:当季同比",
                  "GDP:不变价:其他行业:当季同比"]
# GDP_multiindustries_data_dict = dict(zip(Wind_id_list,Wind_name_list))
#
# GDP_multi_industries = {}
# GDP_multi_industries["name"] = "GDP_multi_industries_yoy"
# GDP_multi_industries["value"] = GDP_multiindustries_data_dict

Total_data["GDP_multi_industries_yoy"] = Convert_list_to_pre_json_data("GDP分行业同比",Wind_id_list,Wind_name_list)


Wind_id_list = ["M0000545", "M0000546", "M0000547", "M0096211", "M0096212", "M0096213", "M0330955"]
Wind_name_list = ["工业增加值:当月同比", "工业增加值:轻工业:当月同比", "工业增加值:重工业:当月同比",
                "工业增加值:采矿业:当月同比", "工业增加值:制造业:当月同比", "工业增加值:电力、燃气及水的生产和供应业:当月同比",
                "工业增加值:高技术产业:当月同比"]

Total_data["Industrial_Production_yoy"] = Convert_list_to_pre_json_data("工业增加值同比",Wind_id_list,Wind_name_list)


Wind_id_list = ["M5767203", "M6001405"]
Wind_name_list = ["服务业生产指数:当月同比", "服务业生产指数:累计同比"]

Total_data["Service_Industry_yoy"] = Convert_list_to_pre_json_data("服务业同比",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0017126", "M0017127", "M0017128", "M0017129", "M0017130", "M0017131",
                "M0017132", "M0017133", "M5766711", "M0017134", "M0017135", "M0017136",
                "M0017137", "M5207790"]

Wind_name_list = ["PMI", "PMI:生产", "PMI:新订单", "PMI:新出口订单", "PMI:在手订单", "PMI:产成品库存",
                  "PMI:采购量", "PMI:进口", "PMI:出厂价格", "PMI:主要原材料购进价格", "PMI:原材料库存",
                  "PMI:从业人员", "PMI:供货商配送时间", "PMI:生产经营活动预期"]

Total_data["PMI"] = Convert_list_to_pre_json_data("PMI",Wind_id_list,Wind_name_list)

Wind_id_list = ["M5206738", "M5206739", "M5206740"]
Wind_name_list = ["PMI:大型企业", "PMI:中型企业", "PMI:小型企业"]

Total_data["PMI by size"] = Convert_list_to_pre_json_data("PMI-按照企业规模",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0048236", "M5207838", "M5207831"]
Wind_name_list = ["非制造业PMI:商务活动", "非制造业PMI:服务业", "非制造业PMI:建筑业"]
Total_data["PMI Non Manufacturing"] = Convert_list_to_pre_json_data("PMI 非制造业",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0000138", "M0061603", "M0290204"]
Wind_name_list = ["财新中国PMI", "财新中国服务业PMI:经营活动指数", "财新中国综合PMI:产出指数"]
Total_data["PMI by Caixin"]  = Convert_list_to_pre_json_data("财新PMI",Wind_id_list,Wind_name_list)


Wind_id_list = ["M0017126", "M0000138", "M5809944", "M0290204"]
Wind_name_list = ["PMI", "财新中国PMI", "中国综合PMI:产出指数", "财新中国综合PMI:产出指数"]
Total_data["PMI NBS vs Caixin"] = Convert_list_to_pre_json_data("统计局与财新PMI",Wind_id_list,Wind_name_list)


Wind_id_list = ["M0000273", "S0029657"]
Wind_name_list = ["固定资产投资完成额:累计同比", "房地产开发投资完成额:累计同比"]
Total_data["Fixed Asset Investment"] = Convert_list_to_pre_json_data("固定资产投资",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0001428", "M0061657", "M0061658"]
Wind_name_list = ["社会消费品零售总额:当月同比", "社会消费品零售总额:城镇:当月同比", "社会消费品零售总额:乡村:当月同比"]
Total_data["Retail Sales of Consumer Goods"] = Convert_list_to_pre_json_data("社会消费品零售总额同比",Wind_id_list,Wind_name_list)


# 房地产

Wind_id_list = ["S0029657","S0073293","S0049591","S0073300"]
Wind_name_list = ["房地产开发投资完成额:累计同比","房屋新开工面积:累计同比","商品房销售额:累计同比","商品房销售面积:累计同比"]
Total_data["Real Estate Construction and Sales"] = Convert_list_to_pre_json_data("房地产开发与销售",Wind_id_list,Wind_name_list)

Wind_id_list = ["S0029672","S0029673"]
Wind_name_list = ["商品房待售面积:累计值","商品房待售面积:累计同比"]
Total_data["Home Inventory"] = Convert_list_to_pre_json_data("商品房库存",Wind_id_list,Wind_name_list)





# 产能

Wind_id_list = ["M5792266"]
Wind_name_list = ["工业产能利用率:当季值"]
Total_data["Industry Capacity Utilizaiton"] = Convert_list_to_pre_json_data("产能利用率",Wind_id_list,Wind_name_list)


Wind_id_list = ["M5792272","M5804701","M5804710","M5804707","M5792271","M5804704","M5804703","M5804711","M5792269",
                "M5804713","M5804706","M5804708","M5792268","M5804709","M5804705","M5804712","M5804702","M5804700"]
Wind_name_list = ["产能利用率:专用设备制造业:当季值","产能利用率:制造业:当季值","产能利用率:有色金属冶炼及压延加工业:当季值",
                  "产能利用率:医药制造业:当季值","产能利用率:通用设备制造业:当季值","产能利用率:食品制造业:当季值",
                  "产能利用率:石油和天然气开采业:当季值","产能利用率:汽车制造业:当季值","产能利用率:煤炭开采和洗选业:当季值",
                  "产能利用率:计算机、通信和其他电子设备制造业:当季值","产能利用率:化学原料及化学制品制造业:当季值",
                  "产能利用率:化学纤维制造业:当季值","产能利用率:黑色金属冶炼及压延加工业:当季值",
                  "产能利用率:非金属矿物制品业:当季值","产能利用率:纺织业:当季值","产能利用率:电气机械和器材制造业:当季值",
                  "产能利用率:电力、热力、燃气及水生产和供应业:当季值","产能利用率:采矿业:当季值",]
Total_data["SubIndustry Capacity Utilization"] = Convert_list_to_pre_json_data("分行业产能利用率",Wind_id_list,Wind_name_list)

# 库存

Wind_id_list = ["M0289288","M0000561"]
Wind_name_list = ["工业企业:存货:累计同比","工业企业:产成品存货:累计同比"]
Total_data["Industry Inventory"] = Convert_list_to_pre_json_data("存货",Wind_id_list,Wind_name_list)


Wind_id_list = ["M0000555","M5767812","M5767814","M0044690","M0044703","M0000557","M0044688","M0289288",
                "M0000561","M0044686"]
Wind_name_list = ["工业企业:主营业务收入:累计同比","工业企业:营业收入:累计同比","工业企业:营业成本:累计同比",
                  "工业企业:销售费用:累计同比","工业企业:利息费用:累计同比","工业企业:利润总额:累计同比",
                  "工业企业:管理费用:累计同比","工业企业:存货:累计同比","工业企业:产成品存货:累计同比",
                  "工业企业:财务费用:累计同比",]
Total_data["Industry Condition"] = Convert_list_to_pre_json_data("工业企业状态",Wind_id_list,Wind_name_list)



write_json_to_file("chart_data.json",Total_data)




