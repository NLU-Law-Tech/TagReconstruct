#coding=UTF-8
import unittest
import sys
sys.path.append('../')
from TagReconstruct import SearchInContext,SearchNearby

searchNearby = SearchNearby('position_list.txt')
searchInContext = SearchInContext('company_list.txt')


class TestTagReconstruct(unittest.TestCase):
    def test_SearchNearby(self):
        context = "王小明是公司實際負責人"
        new_tag = searchNearby.run(context=context,start_at=9,end_at=12,bound=3)
        self.assertEqual(new_tag,"實際負責人")
    
    def test_SearchInContext_a(self):
        context = "炎隆鐵工廠有限公司下稱炎隆"
        new_tag = searchInContext.run(context=context,tag='炎隆',bound=10)
        self.assertEqual(new_tag,"炎隆鐵工廠有限公司")
    
    def test_SearchInContext_b(self):
        context = "華新行實業股份有限公司下稱華實公司"
        new_tag = searchInContext.run(context=context,tag='華實公司',bound=10)
        self.assertEqual(new_tag,"華新行實業股份有限公司")
    
    def test_SearchInContext_b(self):
        context = "這是一段干擾這是一段干擾華新行實業股份有限公司下稱華實公司這這是一段干擾這是一段干擾華實公司"
        new_tag = searchInContext.run(context=context,tag='華實公司',bound=10)
        self.assertEqual(new_tag,"華新行實業股份有限公司")  

if __name__ == '__main__':
    unittest.main()

