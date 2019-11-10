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










write_json_to_file("chart_data.json",Total_data)



