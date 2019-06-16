#!/usr/bin/env python
# encoding: utf-8

row_data = [
    {
        'images': [
            'goods_front/1_P_1449024889889.jpg',
            'goods_front/1_P_1449024889264.jpg',
            'goods_front/1_P_1449024889726.jpg',
            'goods_front/1_P_1449024889018.jpg',
            'goods_front/1_P_1449024889287.jpg'
        ],
        'goods_category': [
            '首页',
            '生鲜食品',
            '根茎类'
        ],
        'market_price': '232',
        'name': '新鲜水果甜蜜香脆单果约800克',
        'desc': '食用百香果可以增加胃部饱腹感，减少余热量的摄入，还可以吸附胆固醇和胆汁之类有机分子，抑制人体对脂肪的吸收。因此，长期食用有利于改善人体营养吸收结构，降低体内脂肪，塑造健康优美体态。',
        'sale_price': '156',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/2_P_1448945810202.jpg',
            'goods_front/2_P_1448945810814.jpg'
        ],
        'goods_category': [
            '首页',
            '生鲜食品',
            '海鲜水产'
        ],
        'market_price': '106',
        'name': '田然牛肉大黄瓜条生鲜牛肉冷冻真空黄牛',
        'desc': '前腿+后腿+羊排共8斤，原生态大山放牧羊羔，曾经的皇室贡品，央视推荐，2005年北京招待全球财金首脑。五层专用包装箱+真空包装+冰袋+保鲜箱+顺丰冷链发货，路途保质期8天',
        'sale_price': '88',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/7_P_1448945104883.jpg',
            'goods_front/7_P_1448945104734.jpg'
        ],
        'goods_category': [
            '首页',
            '生鲜食品',
            '叶菜类'
        ],
        'market_price': '286',
        'name': '酣畅家庭菲力牛排10片澳洲生鲜牛肉团购套餐',
        'desc': None,
        'sale_price': '238',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/47_P_1448946213263.jpg',
            'goods_front/47_P_1448946213157.jpg'
        ],
        'goods_category': [
            '首页',
            '生鲜食品',
            '根茎类'
        ],
        'market_price': '156',
        'name': '日本蒜蓉粉丝扇贝270克6只装',
        'desc': None,
        'sale_price': '108',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/10_P_1448944572085.jpg',
            'goods_front/10_P_1448944572532.jpg',
            'goods_front/10_P_1448944572872.jpg'
        ],
        'goods_category': [
            '首页',
            '生鲜食品',
            '海鲜水产'
        ],
        'market_price': '106',
        'name': '内蒙新鲜牛肉1斤清真生鲜牛肉火锅食材',
        'desc': None,
        'sale_price': '88',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/4_P_1448945381985.jpg',
            'goods_front/4_P_1448945381013.jpg'
        ],
        'goods_category': [
            '首页',
            '生鲜食品',
            '茄果类'
        ],
        'market_price': '90',
        'name': '乌拉圭进口牛肉卷特级肥牛卷',
        'desc': None,
        'sale_price': '75',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/8_P_1448945032810.jpg',
            'goods_front/8_P_1448945032646.jpg'
        ],
        'goods_category': [
            '首页',
            '生鲜食品',
            '进口生鲜'
        ],
        'market_price': '150',
        'name': '五星眼肉牛排套餐8片装原味原切生鲜牛肉',
        'desc': None,
        'sale_price': '125',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/11_P_1448944388277.jpg',
            'goods_front/11_P_1448944388034.jpg',
            'goods_front/11_P_1448944388201.jpg'
        ],
        'goods_category': [
            '首页',
            '生鲜食品',
            '海鲜水产'
        ],
        'market_price': '31',
        'name': '澳洲进口120天谷饲牛仔骨4份原味生鲜',
        'desc': None,
        'sale_price': '26',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/6_P_1448945167279.jpg',
            'goods_front/6_P_1448945167015.jpg'
        ],
        'goods_category': [
            '首页',
            '生鲜食品',
            '菌菇类'
        ],
        'market_price': '239',
        'name': '潮香村澳洲进口牛排家庭团购套餐20片',
        'desc': None,
        'sale_price': '199',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/9_P_1448944791617.jpg',
            'goods_front/9_P_1448944791129.jpg',
            'goods_front/9_P_1448944791077.jpg',
            'goods_front/9_P_1448944791229.jpg'
        ],
        'goods_category': [
            '首页',
            '生鲜食品',
            '根茎类'
        ],
        'market_price': '202',
        'name': '爱食派内蒙古呼伦贝尔冷冻生鲜牛腱子肉1000g',
        'desc': None,
        'sale_price': '168',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/3_P_1448945490837.jpg',
            'goods_front/3_P_1448945490084.jpg'
        ],
        'goods_category': [
            '首页',
            '生鲜食品',
            '精品肉类'
        ],
        'market_price': '306',
        'name': '澳洲进口牛尾巴300g新鲜肥牛肉',
        'desc': '新鲜羊羔肉整只共15斤，原生态大山放牧羊羔，曾经的皇室贡品，央视推荐，2005年北京招待全球财金首脑。五层专用包装箱+真空包装+冰袋+保鲜箱+顺丰冷链发货，路途保质期8天',
        'sale_price': '255',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/48_P_1448943988970.jpg',
            'goods_front/48_P_1448943988898.jpg',
            'goods_front/48_P_1448943988439.jpg'
        ],
        'goods_category': [
            '首页',
            '生鲜食品',
            '海鲜水产'
        ],
        'market_price': '126',
        'name': '新疆巴尔鲁克生鲜牛排眼肉牛扒1200g',
        'desc': None,
        'sale_price': '88',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/5_P_1448945270390.jpg',
            'goods_front/5_P_1448945270067.jpg',
            'goods_front/5_P_1448945270432.jpg'
        ],
        'goods_category': [
            '首页',
            '生鲜食品',
            '蛋制品'
        ],
        'market_price': '144',
        'name': '澳洲进口安格斯牛切片上脑牛排1000g',
        'desc': '澳大利亚是国际公认的没有疯牛病和口蹄疫的国家。为了保持澳大利亚产品的高标准，澳大利亚牛肉业和各级政府共同努力简历了严格的标准和体系，以保证生产的整体化和产品的可追溯性',
        'sale_price': '120',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'images/201705/goods_img/53_P_1495068879687.jpg'
        ],
        'goods_category': [
            '首页',
            '生鲜食品',
            '茄果类'
        ],
        'market_price': '120',
        'name': '帐篷出租',
        'desc': None,
        'sale_price': '100',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/16_P_1448947194687.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '红酒'
        ],
        'market_price': '23',
        'name': '52度茅台集团国隆双喜酒500mlx6',
        'desc': '贵州茅台酒厂（集团）保健酒业有限公司生产，是以“龙”字打头的酒水。中国龙文化上下8000年，源远而流长，龙的形象是一种符号、一种意绪、一种血肉相联的情感。',
        'sale_price': '19',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/14_P_1448947354031.jpg',
            'goods_front/14_P_1448947354433.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '饮料/水'
        ],
        'market_price': '43',
        'name': '52度水井坊臻酿八號500ml',
        'desc': None,
        'sale_price': '36',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/12_P_1448947547989.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '其他酒品'
        ],
        'market_price': '190',
        'name': '53度茅台仁酒500ml',
        'desc': None,
        'sale_price': '158',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/46_P_1448946598711.jpg',
            'goods_front/46_P_1448946598301.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '葡萄酒'
        ],
        'market_price': '38',
        'name': '双响炮洋酒JimBeamwhiskey美国白占边',
        'desc': None,
        'sale_price': '28',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/21_P_1448946793276.jpg',
            'goods_front/21_P_1448946793153.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '饮料/水'
        ],
        'market_price': '55',
        'name': '西夫拉姆进口洋酒小酒版',
        'desc': None,
        'sale_price': '46',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/15_P_1448947257324.jpg',
            'goods_front/15_P_1448947257580.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '洋酒'
        ],
        'market_price': '22',
        'name': '茅台53度飞天茅台500ml',
        'desc': None,
        'sale_price': '18',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/13_P_1448947460386.jpg',
            'goods_front/13_P_1448947460276.jpg',
            'goods_front/13_P_1448947460353.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '葡萄酒'
        ],
        'market_price': '42',
        'name': '52度兰陵·紫气东来1600mL山东名酒',
        'desc': None,
        'sale_price': '35',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/50_P_1448946543091.jpg',
            'goods_front/50_P_1448946542182.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '饮料/水'
        ],
        'market_price': '24',
        'name': 'JohnnieWalker尊尼获加黑牌威士忌',
        'desc': None,
        'sale_price': '20',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/51_P_1448946466595.jpg',
            'goods_front/51_P_1448946466208.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '洋酒'
        ],
        'market_price': '31',
        'name': '人头马CLUB特优香槟干邑350ml',
        'desc': None,
        'sale_price': '26',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/17_P_1448947102246.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '啤酒'
        ],
        'market_price': '54',
        'name': '张裕干红葡萄酒750ml*6支',
        'desc': None,
        'sale_price': '45',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/20_P_1448946850602.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '葡萄酒'
        ],
        'market_price': '46',
        'name': '原瓶原装进口洋酒烈酒法国云鹿XO白兰地',
        'desc': None,
        'sale_price': '38',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/19_P_1448946951581.jpg',
            'goods_front/19_P_1448946951726.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '白酒'
        ],
        'market_price': '82',
        'name': '法国原装进口圣贝克干红葡萄酒750ml',
        'desc': None,
        'sale_price': '68',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/18_P_1448947011435.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '白酒'
        ],
        'market_price': '67',
        'name': '法国百利威干红葡萄酒AOP级6支装',
        'desc': None,
        'sale_price': '56',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/22_P_1448946729629.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '洋酒'
        ],
        'market_price': '71',
        'name': '芝华士12年苏格兰威士忌700ml',
        'desc': None,
        'sale_price': '59',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/45_P_1448946661303.jpg'
        ],
        'goods_category': [
            '首页',
            '酒水饮料',
            '饮料/水'
        ],
        'market_price': '31',
        'name': '深蓝伏特加巴维兰利口酒送预调酒',
        'desc': None,
        'sale_price': '18',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/32_P_1448948525620.jpg'
        ],
        'goods_category': [
            '首页',
            '蔬菜水果',
            '精选蔬菜'
        ],
        'market_price': '43',
        'name': '赣南脐橙特级果10斤装',
        'desc': None,
        'sale_price': '36',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/30_P_1448948663450.jpg',
            'goods_front/30_P_1448948662571.jpg',
            'goods_front/30_P_1448948663221.jpg'
        ],
        'goods_category': [
            '首页',
            '蔬菜水果',
            '进口水果'
        ],
        'market_price': '11',
        'name': '泰国菠萝蜜16-18斤1个装',
        'desc': '【懒人吃法】菠萝蜜果肉，冰袋保鲜，收货就吃，冰爽Q脆甜，2斤装，全国顺丰空运包邮，发出后48小时内可达，一线城市基本隔天可达',
        'sale_price': '9',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/31_P_1448948598947.jpg',
            'goods_front/31_P_1448948598475.jpg'
        ],
        'goods_category': [
            '首页',
            '蔬菜水果',
            '国产水果'
        ],
        'market_price': '22',
        'name': '四川双流草莓新鲜水果礼盒2盒',
        'desc': None,
        'sale_price': '18',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/35_P_1448948333610.jpg',
            'goods_front/35_P_1448948333313.jpg'
        ],
        'goods_category': [
            '首页',
            '蔬菜水果',
            '有机蔬菜'
        ],
        'market_price': '67',
        'name': '新鲜头茬非洲冰草冰菜',
        'desc': None,
        'sale_price': '56',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/36_P_1448948234405.jpg',
            'goods_front/36_P_1448948234250.jpg'
        ],
        'goods_category': [
            '首页',
            '蔬菜水果',
            '有机蔬菜'
        ],
        'market_price': '6',
        'name': '仿真蔬菜水果果蔬菜模型',
        'desc': None,
        'sale_price': '5',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/33_P_1448948479966.jpg',
            'goods_front/33_P_1448948479886.jpg'
        ],
        'goods_category': [
            '首页',
            '蔬菜水果',
            '精选蔬菜'
        ],
        'market_price': '28',
        'name': '现摘芭乐番石榴台湾珍珠芭乐',
        'desc': '''海南产精品释迦果,
        释迦是水果中的贵族,
        产量少,
        味道很甜,
        奶香十足,
        非常可口,
        果裹果园顺丰空运,
        保证新鲜.果子个大,
        一斤1-2个左右,
        大个头的果子更尽兴!
        ''',
        'sale_price': '23',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/34_P_1448948399009.jpg'
        ],
        'goods_category': [
            '首页',
            '蔬菜水果',
            '国产水果'
        ],
        'market_price': '46',
        'name': '潍坊萝卜5斤/箱礼盒',
        'desc': '脐橙规格是65-90MM左右（标准果果径平均70MM左右，精品果果径平均80MM左右），一斤大概有2-4个左右，脐橙产自江西省赣州市信丰县安西镇，全过程都是采用农家有机肥种植，生态天然',
        'sale_price': '38',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/43_P_1448948762645.jpg'
        ],
        'goods_category': [
            '首页',
            '休闲食品'
        ],
        'market_price': '154',
        'name': '休闲零食膨化食品焦糖/奶油/椒麻味',
        'desc': None,
        'sale_price': '99',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/38_P_1448949220255.jpg'
        ],
        'goods_category': [
            '首页',
            '奶类食品',
            '奶粉'
        ],
        'market_price': '84',
        'name': '蒙牛未来星儿童成长牛奶骨力型190ml*15盒',
        'desc': None,
        'sale_price': '70',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/44_P_1448948850187.jpg'
        ],
        'goods_category': [
            '首页',
            '奶类食品',
            '进口奶品'
        ],
        'market_price': '70',
        'name': '蒙牛特仑苏有机奶250ml×12盒',
        'desc': None,
        'sale_price': '32',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'images/201511/goods_img/49_P_1448162819889.jpg'
        ],
        'goods_category': [
            '首页',
            '奶类食品'
        ],
        'market_price': '1',
        'name': '1支付测试商品',
        'desc': None,
        'sale_price': '1',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/40_P_1448949038702.jpg'
        ],
        'goods_category': [
            '首页',
            '奶类食品',
            '进口奶品'
        ],
        'market_price': '70',
        'name': '德运全脂新鲜纯牛奶1L*10盒装整箱',
        'desc': None,
        'sale_price': '58',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/39_P_1448949115481.jpg'
        ],
        'goods_category': [
            '首页',
            '奶类食品',
            '有机奶'
        ],
        'market_price': '38',
        'name': '木糖醇红枣早餐奶即食豆奶粉538g',
        'desc': None,
        'sale_price': '32',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/41_P_1448948980358.jpg'
        ],
        'goods_category': [
            '首页',
            '奶类食品',
            '原料奶'
        ],
        'market_price': '26',
        'name': '高钙液体奶200ml*24盒',
        'desc': None,
        'sale_price': '22',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/37_P_1448949284365.jpg'
        ],
        'goods_category': [
            '首页',
            '奶类食品',
            '国产奶品'
        ],
        'market_price': '720',
        'name': '新西兰进口全脂奶粉900g',
        'desc': None,
        'sale_price': '600',
        'goods_desc':'值得推荐'
    },
    {
        'images': [
            'goods_front/42_P_1448948895193.jpg'
        ],
        'goods_category': [
            '首页',
            '奶类食品',
            '进口奶品'
        ],
        'market_price': '43',
        'name': '伊利官方直营全脂营养舒化奶250ml*12盒*2提',
        'desc': None,
        'sale_price': '36',
        'goods_desc':'值得推荐'
    },
{
        'sale_price': '156',
        'images': [
            'goods_front/27_P_1448947771805.jpg'
        ],
        'market_price': '187',
        'goods_category': [
            '首页',
            '粮油副食',
            '厨房调料'
        ],
        'desc': None,
        'name': '维纳斯橄榄菜籽油5L/桶',
        'goods_desc':'值得推荐'
    },
    {
        'sale_price': '15',
        'images': [
            'goods_front/23_P_1448948070348.jpg'
        ],
        'market_price': '18',
        'goods_category': [
            '首页',
            '粮油副食',
            '食用油'
        ],
        'desc': None,
        'name': '糙米450gx3包粮油米面',
        'goods_desc':'值得推荐'
    },
    {
        'sale_price': '45',
        'images': [
            'goods_front/26_P_1448947825754.jpg'
        ],
        'market_price': '54',
        'goods_category': [
            '首页',
            '粮油副食',
            '调味品'
        ],
        'desc': None,
        'name': '精炼一级大豆油5L色拉油粮油食用油',
        'goods_desc':'值得推荐'
    },
    {
        'sale_price': '26',
        'images': [
            'goods_front/28_P_1448947699948.jpg',
            'goods_front/28_P_1448947699777.jpg'
        ],
        'market_price': '31',
        'goods_category': [
            '首页',
            '粮油副食',
            '南北干货'
        ],
        'desc': None,
        'name': '橄榄玉米油5L*2桶',
        'goods_desc':'值得推荐'
    },
    {
        'sale_price': '9',
        'images': [
            'goods_front/24_P_1448948023823.jpg',
            'goods_front/24_P_1448948023977.jpg'
        ],
        'market_price': '11',
        'goods_category': [
            '首页',
            '粮油副食',
            '方便速食'
        ],
        'desc': None,
        'name': '山西黑米农家黑米4斤',
        'goods_desc':'值得推荐'
    },
    {
        'sale_price': '12',
        'images': [
            'goods_front/25_P_1448947875346.jpg'
        ],
        'market_price': '14',
        'goods_category': [
            '首页',
            '粮油副食',
            '米面杂粮'
        ],
        'desc': None,
        'name': '稻园牌稻米油粮油米糠油绿色植物油',
        'goods_desc':'值得推荐'
    },
    {
        'sale_price': '12',
        'images': [
            'goods_front/29_P_1448947631994.jpg'
        ],
        'market_price': '14',
        'goods_category': [
            '首页',
            '粮油副食',
            '食用油'
        ],
        'desc': None,
        'name': '融氏纯玉米胚芽油5l桶',
        'goods_desc':'值得推荐'
    }
]

pass