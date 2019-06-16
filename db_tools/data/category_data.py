#!/usr/bin/env python
# encoding: utf-8

row_data = [
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': 'yr',
                        'name': '羊肉'
                    },
                    {
                        'code': 'ql',
                        'name': '禽类'
                    },
                    {
                        'code': 'zr',
                        'name': '猪肉'
                    },
                    {
                        'code': 'nr',
                        'name': '牛肉'
                    }
                ],
                'code': 'jprl',
                'name': '精品肉类'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'cb',
                        'name': '参鲍'
                    },
                    {
                        'code': 'yu',
                        'name': '鱼'
                    },
                    {
                        'code': 'xia',
                        'name': '虾'
                    },
                    {
                        'code': 'xb',
                        'name': '蟹/贝'
                    }
                ],
                'code': 'hxsc',
                'name': '海鲜水产'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'xhd_xyd',
                        'name': '松花蛋/咸鸭蛋'
                    },
                    {
                        'code': 'jd',
                        'name': '鸡蛋'
                    }
                ],
                'code': 'dzp',
                'name': '蛋制品'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'sc',
                        'name': '生菜'
                    },
                    {
                        'code': 'bc',
                        'name': '菠菜'
                    },
                    {
                        'code': 'yj',
                        'name': '圆椒'
                    },
                    {
                        'code': 'xlh',
                        'name': '西兰花'
                    }
                ],
                'code': 'ycl',
                'name': '叶菜类'
            },
            {
                'sub_categorys': [

                ],
                'code': 'gjl',
                'name': '根茎类'
            },
            {
                'sub_categorys': [

                ],
                'code': 'qgl',
                'name': '茄果类'
            },
            {
                'sub_categorys': [

                ],
                'code': 'jgl',
                'name': '菌菇类'
            },
            {
                'sub_categorys': [

                ],
                'code': 'jksx',
                'name': '进口生鲜'
            }
        ],
        'code': 'sxsp',
        'name': '生鲜食品'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': 'wly',
                        'name': '五粮液'
                    },
                    {
                        'code': 'lzlj',
                        'name': '泸州老窖'
                    },
                    {
                        'code': 'mt',
                        'name': '茅台'
                    }
                ],
                'code': 'bk',
                'name': '白酒'
            },
            {
                'sub_categorys': [

                ],
                'code': 'ptj',
                'name': '葡萄酒'
            },
            {
                'sub_categorys': [

                ],
                'code': 'yj',
                'name': '洋酒'
            },
            {
                'sub_categorys': [

                ],
                'code': 'pj',
                'name': '啤酒'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'qtpp',
                        'name': '其他品牌'
                    },
                    {
                        'code': 'hj',
                        'name': '黄酒'
                    },
                    {
                        'code': 'ysj',
                        'name': '养生酒'
                    }
                ],
                'code': 'qtjp',
                'name': '其他酒品'
            },
            {
                'sub_categorys': [

                ],
                'code': 'yls',
                'name': '饮料/水'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'bld',
                        'name': '白兰地'
                    },
                    {
                        'code': 'wsj',
                        'name': '威士忌'
                    }
                ],
                'code': 'hj',
                'name': '红酒'
            }
        ],
        'code': 'jsyl',
        'name': '酒水饮料'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': 'qtsyy',
                        'name': '其他食用油'
                    },
                    {
                        'code': 'czy',
                        'name': '菜仔油'
                    },
                    {
                        'code': 'hsy',
                        'name': '花生油'
                    },
                    {
                        'code': 'gly',
                        'name': '橄榄油'
                    },
                    {
                        'code': 'lh',
                        'name': '礼盒'
                    }
                ],
                'code': 'syy',
                'name': '食用油'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'mf/mt',
                        'name': '面粉/面条'
                    },
                    {
                        'code': 'dm',
                        'name': '大米'
                    },
                    {
                        'code': 'ydlm',
                        'name': '意大利面'
                    }
                ],
                'code': 'mmzl',
                'name': '米面杂粮'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'twy/z',
                        'name': '调味油/汁'
                    },
                    {
                        'code': 'jy/c',
                        'name': '酱油/醋'
                    }
                ],
                'code': 'cftl',
                'name': '厨房调料'
            },
            {
                'sub_categorys': [

                ],
                'code': 'nbgh',
                'name': '南北干货'
            },
            {
                'sub_categorys': [

                ],
                'code': 'fbss',
                'name': '方便速食'
            },
            {
                'sub_categorys': [

                ],
                'code': 'twp',
                'name': '调味品'
            }
        ],
        'code': 'lyfs',
        'name': '粮油副食'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': 'xhs',
                        'name': '西红柿'
                    },
                    {
                        'code': 'jc',
                        'name': '韭菜'
                    },
                    {
                        'code': 'qc',
                        'name': '青菜'
                    }
                ],
                'code': 'yjsc',
                'name': '有机蔬菜'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'gl',
                        'name': '甘蓝'
                    },
                    {
                        'code': 'hlb',
                        'name': '胡萝卜'
                    },
                    {
                        'code': 'hg',
                        'name': '黄瓜'
                    }
                ],
                'code': 'jxsc',
                'name': '精选蔬菜'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'hlg',
                        'name': '火龙果'
                    },
                    {
                        'code': 'blm',
                        'name': '菠萝蜜'
                    },
                    {
                        'code': 'qyg',
                        'name': '奇异果'
                    }
                ],
                'code': 'jksg',
                'name': '进口水果'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'sglh',
                        'name': '水果礼盒'
                    },
                    {
                        'code': 'pg',
                        'name': '苹果'
                    },
                    {
                        'code': 'xl',
                        'name': '雪梨'
                    }
                ],
                'code': 'gcsg',
                'name': '国产水果'
            }
        ],
        'code': 'scsg',
        'name': '蔬菜水果'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': 'gd',
                        'name': '果冻'
                    },
                    {
                        'code': 'zl',
                        'name': '枣类'
                    },
                    {
                        'code': 'mj',
                        'name': '蜜饯'
                    },
                    {
                        'code': 'rlls',
                        'name': '肉类零食'
                    },
                    {
                        'code': 'jgch',
                        'name': '坚果炒货'
                    }
                ],
                'code': 'xxls',
                'name': '休闲零食'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'cyxt',
                        'name': '创意喜糖'
                    },
                    {
                        'code': 'kxt',
                        'name': '口香糖'
                    },
                    {
                        'code': 'rt',
                        'name': '软糖'
                    },
                    {
                        'code': 'bbt',
                        'name': '棒棒糖'
                    }
                ],
                'code': 'tg',
                'name': '糖果'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'jxqkl',
                        'name': '夹心巧克力'
                    },
                    {
                        'code': 'bqkl',
                        'name': '白巧克力'
                    },
                    {
                        'code': 'slqkl',
                        'name': '松露巧克力'
                    },
                    {
                        'code': 'hqkl',
                        'name': '黑巧克力'
                    }
                ],
                'code': 'qkl',
                'name': '巧克力'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'nrg',
                        'name': '牛肉干'
                    },
                    {
                        'code': 'zrb',
                        'name': '猪肉脯'
                    },
                    {
                        'code': 'nrl',
                        'name': '牛肉粒'
                    },
                    {
                        'code': 'zrg',
                        'name': '猪肉干'
                    }
                ],
                'code': 'rgrp/dg',
                'name': '肉干肉脯/豆干'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'yyz',
                        'name': '鱿鱼足'
                    },
                    {
                        'code': 'yys',
                        'name': '鱿鱼丝'
                    },
                    {
                        'code': 'my/wz',
                        'name': '墨鱼/乌贼'
                    },
                    {
                        'code': 'yyz',
                        'name': '鱿鱼仔'
                    },
                    {
                        'code': 'yyp',
                        'name': '鱿鱼片'
                    }
                ],
                'code': 'yys/yg',
                'name': '鱿鱼丝/鱼干'
            }
        ],
        'code': 'xxsp',
        'name': '休闲食品'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [

                ],
                'code': 'jkmp',
                'name': '进口奶品'
            },
            {
                'sub_categorys': [

                ],
                'code': 'gcmp',
                'name': '国产奶品'
            },
            {
                'sub_categorys': [

                ],
                'code': 'nf',
                'name': '奶粉'
            },
            {
                'sub_categorys': [

                ],
                'code': 'yjn',
                'name': '有机奶'
            },
            {
                'sub_categorys': [

                ],
                'code': 'yln',
                'name': '原料奶'
            }
        ],
        'code': 'nlsp',
        'name': '奶类食品'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [

                ],
                'code': 'jgl',
                'name': '菌菇类'
            },
            {
                'sub_categorys': [

                ],
                'code': 'yghc',
                'name': '腌干海产'
            },
            {
                'sub_categorys': [

                ],
                'code': 'tl',
                'name': '汤料'
            },
            {
                'sub_categorys': [

                ],
                'code': 'dl',
                'name': '豆类'
            },
            {
                'sub_categorys': [

                ],
                'code': 'gc/cg',
                'name': '干菜/菜干'
            },
            {
                'sub_categorys': [

                ],
                'code': 'gg/gg',
                'name': '干果/果干'
            },
            {
                'sub_categorys': [

                ],
                'code': 'dzp',
                'name': '豆制品'
            },
            {
                'sub_categorys': [

                ],
                'code': 'lw',
                'name': '腊味'
            }
        ],
        'code': 'trgh',
        'name': '天然干货'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [

                ],
                'code': 'bc',
                'name': '白茶'
            },
            {
                'sub_categorys': [

                ],
                'code': 'hc',
                'name': '红茶'
            },
            {
                'sub_categorys': [

                ],
                'code': 'lc',
                'name': '绿茶'
            }
        ],
        'code': 'qxmc',
        'name': '精选茗茶'
    }
]