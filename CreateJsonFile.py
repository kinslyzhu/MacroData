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


# 国有企业 vs 民营企业

Wind_id_list = ["M0049819","M0000557"]
Wind_name_list = ["全国国有企业:利润总额:累计同比","工业企业:利润总额:累计同比"]
Total_data["Industry Profit"] = Convert_list_to_pre_json_data("工业企业利润",Wind_id_list,Wind_name_list)

# 居民收入

Wind_id_list = ["M0024149","M5405765"]
Wind_name_list = ["就业人员平均工资:城镇单位:累计同比","农村外出务工劳动力:月均收入:同比"]
Total_data["Citizen Income"] = Convert_list_to_pre_json_data("居民收入",Wind_id_list,Wind_name_list)


Wind_id_list=["M5405764"]
Wind_name_list = ["农村外出务工劳动力:月均收入"]
Total_data["Migrant Worker"] = Convert_list_to_pre_json_data("农民工月均收入",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0012989","M0012990"]
Wind_name_list = ["城镇居民人均可支配收入:累计同比","城镇居民人均可支配收入:实际累计同比"]
Total_data["Per Capita Disposable Income of Urban Resident"] = Convert_list_to_pre_json_data("城镇居民人均可支配收入",Wind_id_list,Wind_name_list)


# 对外贸易
Wind_id_list = ["M0000605","M0000607","M0000609"]
Wind_name_list = ["进出口金额:当月同比","出口金额:当月同比","进口金额:当月同比"]
Total_data["Import and Export Trade"] = Convert_list_to_pre_json_data("进出口金额",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0000610"]
Wind_name_list = ["贸易差额:当月值"]
Total_data["Trade Surplus"] = Convert_list_to_pre_json_data("贸易差额",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0007453","M0007454"]
Wind_name_list = ["工业企业:出口交货值:当月值","工业企业:出口交货值:当月同比"]
Total_data["Export Goods Value of Industry"] = Convert_list_to_pre_json_data("工业企业出口交货值",Wind_id_list,Wind_name_list)


Wind_id_list = ["M5540037","M5540038","M5540039"]
Wind_name_list = ["国际货物和服务贸易差额:当月值","国际货物和服务贸易贷方:当月值","国际货物和服务贸易借方:当月值"]
Total_data["International Goods and Service Trade"] = Convert_list_to_pre_json_data("国际货物和服务贸易",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0009870","M5405461"]
Wind_name_list = ["实际使用外资金额:外商直接投资:当月值","实际使用外资金额:合计:累计同比"]
Total_data["FDI"]  = Convert_list_to_pre_json_data("FDI",Wind_id_list,Wind_name_list)

Wind_id_list = ["M7049801","M5200016"]
Wind_name_list = ["对外全行业直接投资:累计同比","非金融类对外直接投资:累计同比"]
Total_data["Domestic Direct Investment"] = Convert_list_to_pre_json_data("对外投资",Wind_id_list,Wind_name_list)

Wind_id_list = ["M5206847","M5206870"]
Wind_name_list = ["差额:经常项目:当季值","差额:资本和金融项目:当季值"]
Total_data["Current and Capital Account"] = Convert_list_to_pre_json_data("经常项目与资本项目",Wind_id_list,Wind_name_list)

# 货币与债务

Wind_id_list = ["M0010049"]
Wind_name_list = ["官方储备资产:外汇储备"]
Total_data["Foreign Currency Reserve"] = Convert_list_to_pre_json_data("外汇储备",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0010048"]
Wind_name_list = ["官方储备资产:黄金(以盎司计算的纯金数量)"]
Total_data["Gold Reserve"] = Convert_list_to_pre_json_data("黄金储备",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0327899"]
Wind_name_list = ["金融机构:人民币:资金运用:中央银行外汇占款"]
Total_data["Position for Forex Purchase"] = Convert_list_to_pre_json_data("外汇占款",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0024339"]
Wind_name_list = ["外债余额"]
Total_data["Foreign Debt"] = Convert_list_to_pre_json_data("外债余额",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0024342","M0024343"]
Wind_name_list = ["中长期债务:占外债余额比例","短期债务:占外债余额比例"]
Total_data["Debt Structure"] = Convert_list_to_pre_json_data("债务比例",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0046169","M0089129","M0089130"]
Wind_name_list = ["公共财政收入:累计同比","中央财政收入:累计同比","地方本级财政收入:累计同比"]
Total_data["Growth of Govt Revenue"] = Convert_list_to_pre_json_data("财政收入增速",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0043411"]
Wind_name_list = ["金融机构:财政存款余额"]
Total_data["Fiscal Deposit"] = Convert_list_to_pre_json_data("财政存款余额",Wind_id_list,Wind_name_list)


Wind_id_list = ["M5658447"]
Wind_name_list = ["地方政府债务余额"]
Total_data["Local Govt Debt"] = Convert_list_to_pre_json_data("地方政府债务余额",Wind_id_list,Wind_name_list)


Wind_id_list = ["M0001381","M0001383","M0001385"]
Wind_name_list = ["M0:同比","M1:同比","M2:同比"]
Total_data["M0 M1 M2"] = Convert_list_to_pre_json_data("货币统计增速",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0001380","M0001382","M0001384"]
Wind_name_list = ["M0","M1","M2"]
Total_data["Curreny and Cash"] = Convert_list_to_pre_json_data("货币统计",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0009973","M5206730"]
Wind_name_list = ["金融机构:新增人民币贷款:当月值","社会融资规模:当月值"]
Total_data["Financing Scale"] = Convert_list_to_pre_json_data("融资规模",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0061615","M0061614"]
Wind_name_list = ["公开市场操作:货币投放","公开市场操作:货币净投放"]
Total_data["Open Market Operation"] = Convert_list_to_pre_json_data("公开市场操作",Wind_id_list,Wind_name_list)

Wind_id_list = ["M5528818"]
Wind_name_list = ["中期借贷便利(MLF):投放:当月值"]
Total_data["MLF Volume"] = Convert_list_to_pre_json_data("MLF Volume",Wind_id_list,Wind_name_list)

Wind_id_list = ["M5528820","M5543249","M5543248"]
Wind_name_list = ["中期借贷便利(MLF):利率","中期借贷便利(MLF):利率:1年","中期借贷便利(MLF):利率:6个月"]
Total_data["MLF Price"] = Convert_list_to_pre_json_data("MLF Price",Wind_id_list,Wind_name_list)

Wind_id_list = ["M5528821","M5528822"]
Wind_name_list = ["抵押补充贷款(PSL):提供资金:当月新增","抵押补充贷款(PSL):期末余额"]
Total_data["PSL"] = Convert_list_to_pre_json_data("PSL",Wind_id_list,Wind_name_list)

# 利率

Wind_id_list = ["M0017146"]
Wind_name_list = ["7天回购利率:加权平均:最近1周(B1W)"]
Total_data["Repo"] = Convert_list_to_pre_json_data("7天逆回购",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0017142"]
Wind_name_list = ["SHIBOR:3个月"]
Total_data["Shibor"] = Convert_list_to_pre_json_data("Shibor 3M",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0058002","M0058003","M0058004","M0058005"]
Wind_name_list = ["金融机构人民币贷款加权平均利率","金融机构人民币贷款加权平均利率:一般贷款","金融机构人民币贷款加权平均利率:票据融资","金融机构人民币贷款加权平均利率:个人住房贷款"]
Total_data["Loan Interest Rate"] = Convert_list_to_pre_json_data("贷款利率",Wind_id_list,Wind_name_list)

Wind_id_list = ["S0211686"]
Wind_name_list = ["7日年化收益率:余额宝(天弘)"]
Total_data["yuebao"] = Convert_list_to_pre_json_data("余额宝",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0000185","M0290205"]
Wind_name_list = ["中间价:美元兑人民币","USDCNH:即期汇率"]
Total_data["RMB Exchange Rate"] = Convert_list_to_pre_json_data("人民币汇率",Wind_id_list,Wind_name_list)

# 价格

Wind_id_list =["M0000612","M0001227","M0001375"]
Wind_name_list = ["CPI:当月同比","PPI:全部工业品:当月同比","CGPI:当月同比"]
Total_data["CPI vs PPI"] = Convert_list_to_pre_json_data("CPI vs PPI",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0000612","M0000616","M0000613","M0085932","M0096666","M0000614","M0000615"]
Wind_name_list = ["CPI:当月同比","CPI:食品:当月同比","CPI:非食品:当月同比","CPI:不包括食品和能源(核心CPI):当月同比","CPI:不包括鲜菜和鲜果:当月同比","CPI:消费品:当月同比","CPI:服务:当月同比"]
Total_data["CPI"] = Convert_list_to_pre_json_data("CPI",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0001227","M0001228","M0001232"]
Wind_name_list = ["PPI:全部工业品:当月同比","PPI:生产资料:当月同比","PPI:生活资料:当月同比"]
Total_data["PPI"] = Convert_list_to_pre_json_data("PPI",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0001375","M0001376"]
Wind_name_list = ["CGPI:当月同比","CGPI:农产品:当月同比"]
Total_data["CGPI"] = Convert_list_to_pre_json_data("CGPI",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0043829","M0043949"]
Wind_name_list = ["出口价格指数(HS2):总指数","进口价格指数(HS2):总指数"]
Total_data["Trade Price Index"] = Convert_list_to_pre_json_data("进出口价格指数",Wind_id_list,Wind_name_list)

Wind_id_list = ["M5439528"]
Wind_name_list = ["GDP:平减指数:GDP:初步核算:当季同比"]
Total_data["GDP deflator"] = Convert_list_to_pre_json_data("GDP 平减指数",Wind_id_list,Wind_name_list)

Wind_id_list = ["S2707425","S2707403","S2707411"]
Wind_name_list = ["70个大中城市二手住宅价格指数:当月同比","70个大中城市新建住宅价格指数:当月同比","70个大中城市新建商品住宅价格指数:当月同比"]
Total_data["70 Cities Home Price"] = Convert_list_to_pre_json_data("70城价格指数",Wind_id_list,Wind_name_list)

Wind_id_list = ["S2707427","S2707428","S2707429"]
Wind_name_list = ["70个大中城市二手住宅价格指数:一线城市:当月同比","70个大中城市二手住宅价格指数:二线城市:当月同比","70个大中城市二手住宅价格指数:三线城市:当月同比"]
Total_data["70 Cities Home Price by Scale"] = Convert_list_to_pre_json_data("70城价格指数按规模划分",Wind_id_list,Wind_name_list)

Wind_id_list = ["S2707445","S2707446","S2707447"]
Wind_name_list = ["百城住宅价格指数:一线城市:同比","百城住宅价格指数:二线城市:同比","百城住宅价格指数:三线城市:同比"]
Total_data["100 Cities Home Price Index by Scale"] = Convert_list_to_pre_json_data("百城住宅价格指数按规模划分",Wind_id_list,Wind_name_list)

Wind_id_list = ["S2704485"]
Wind_name_list = ["百城住宅价格指数:同比"]
Total_data["100 Cities Home Price Index"] = Convert_list_to_pre_json_data("百城住宅价格指数同比",Wind_id_list,Wind_name_list)

# 人口
Wind_id_list = ["M0028615"]
Wind_name_list = ["总人口"]
Total_data["China Polulation"] = Convert_list_to_pre_json_data("总人口",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0013626","M0013633","M0013640","M0013647","M0013654","M0013661","M0013668","M0013675","M0013682",
                "M0013689","M0013696","M0013703","M0013710","M0013717","M0013724","M0013731","M0013738","M0013745",
                "M0013752","M0013759"]

Wind_name_list = ["抽样数:占总人口比例:0-4岁","抽样数:占总人口比例:5-9岁","抽样数:占总人口比例:10-14岁",
                  "抽样数:占总人口比例:15-19岁","抽样数:占总人口比例:20-24岁","抽样数:占总人口比例:25-29岁",
                  "抽样数:占总人口比例:30-34岁","抽样数:占总人口比例:35-39岁","抽样数:占总人口比例:40-44岁",
                  "抽样数:占总人口比例:45-49岁","抽样数:占总人口比例:50-54岁","抽样数:占总人口比例:55-59岁",
                  "抽样数:占总人口比例:60-64岁","抽样数:占总人口比例:65-69岁","抽样数:占总人口比例:70-74岁",
                  "抽样数:占总人口比例:75-79岁","抽样数:占总人口比例:80-84岁","抽样数:占总人口比例:85-89岁",
                  "抽样数:占总人口比例:90-94岁","抽样数:占总人口比例:95岁以上"]
Total_data["Population Structure"] = Convert_list_to_pre_json_data("人口结构",Wind_id_list,Wind_name_list)

Wind_id_list = ["M6096116"]
Wind_name_list = ["城镇新增就业人数:累计同比"]
Total_data["New Jobs"] = Convert_list_to_pre_json_data("新增就业人数",Wind_id_list,Wind_name_list)

Wind_id_list = ["M0013626","M0013633","M0013640"]
Wind_name_list = ["城镇调查失业率","就业人员调查失业率:25-59岁","31个大城市城镇调查失业率"]
Total_data["Unemployment"] = Convert_list_to_pre_json_data("失业率",Wind_id_list,Wind_name_list)





write_json_to_file("chart_data.json",Total_data)




