#coding=UTF-8
import sys
sys.path.append('../')
from TagReconstruct import SearchInContext,SearchNearby

context = """
123456王小明是公司實際負責人7890
"""
search = SearchNearby('position_list.txt')
new_tag = search.run(context=context,start_at=15,end_at=18,bound=3)
print(context[15:18],new_tag) # 負責人, 實際負責人


context = """
炎隆
某某公司
炎隆鐵工廠有限公司
"""
search = SearchInContext('company_list.txt')
new_tag = search.run(context=context,tag='炎隆',bound=10)
print(new_tag) # 炎隆鐵工廠有限公司
