#coding=UTF-8
import sys
sys.path.append('../')
from TagReconstruct import SearchInContext,SearchNearby

context = """
王小明是公司實際負責人
"""
search = SearchNearby('position_list.txt')
new_tag = search.run(context=context,start_at=9,end_at=12,bound=3)
print(context[9:12],new_tag) # 負責人, 實際負責人


context = """
炎隆鐵工廠有限公司下稱炎隆
"""
search = SearchInContext('company_list.txt')
new_tag = search.run(context=context,tag='炎隆',bound=10)
print(new_tag) # 炎隆鐵工廠有限公司
