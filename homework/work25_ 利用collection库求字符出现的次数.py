'''
-*- coding: utf-8 -*-
@Author  : zy

利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"

'''

import collections

s="kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
print(collections.Counter(s))