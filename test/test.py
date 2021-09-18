#coding=UTF-8
import unittest
import sys

from loguru import logger
sys.path.insert(0,'../')
import TagReconstruct
logger.debug(TagReconstruct)
from TagReconstruct import SearchInContext,SearchNearby

searchNearby = SearchNearby('position_list.txt')
searchInContext = SearchInContext('company_list.txt')


class TestTagReconstruct(unittest.TestCase):
    def test_SearchNearby_a(self):
        context = "王小明是公司實際負責人"
        new_tag = searchNearby.run(context=context,start_at=9,end_at=12,bound=3)
        self.assertEqual(new_tag,"實際負責人")
    
    def test_SearchNearby_b(self):
        context = "王小明是公司業務業務人"
        new_tag = searchNearby.run(context=context,start_at=9,end_at=12,bound=3,tag="負責人")
        self.assertEqual(new_tag,"負責人")
    
    def test_SearchInContext_a(self):
        context = "炎隆鐵工廠有限公司下稱炎隆"
        new_tag = searchInContext.run(context=context,tag='炎隆',bound=10)
        self.assertEqual(new_tag,"炎隆鐵工廠有限公司")
    
    def test_SearchInContext_b(self):
        context = "華新行實業股份有限公司下稱華實公司"
        new_tag = searchInContext.run(context=context,tag='華實公司',bound=10)
        self.assertEqual(new_tag,"華新行實業股份有限公司")
    
    def test_SearchInContext_c(self):
        context = "這是一段干擾這是一段干擾華新行實業股份有限公司下稱華實公司這這是一段干擾這是一段干擾華實公司"
        new_tag = searchInContext.run(context=context,tag='華實公司',bound=10)
        self.assertEqual(new_tag,"華新行實業股份有限公司")  
    
    def test_SearchInContext_d(self):
        context = """
        陶緣海係址設臺北市○○區○○街000號5樓之數位點子多媒
        體股份有限公司（下稱數位點子公司）下線經銷商，從事行
        動電話預付卡行銷業務
        """
        context = context.replace("\n","").replace(" ","")
        new_tag = searchInContext.run(context=context,tag='多媒體股份有限公司123',bound=10)
        self.assertEqual(new_tag,"多媒體股份有限公司123")
    
    def test_SearchInContext_e(self):
        context = """
        陶緣海係址設臺北市○○區○○街000號5樓之數位點子多媒
        體股份有限公司（下稱數位點子公司）下線經銷商，從事行
        動電話預付卡行銷業務
        """
        context = context.replace("\n","").replace(" ","")
        new_tag = searchInContext.run(context=context,tag='多媒體股份有限公司',bound=10)
        self.assertEqual(new_tag,"數位點子多媒體股份有限公司")  

if __name__ == '__main__':
    unittest.main()

