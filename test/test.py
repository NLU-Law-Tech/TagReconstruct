#coding=UTF-8
import unittest
import sys

from loguru import logger
sys.path.insert(0,'../')
import TagReconstruct
logger.debug(TagReconstruct)
from TagReconstruct import SearchInContext,SearchNearby

searchNearby = SearchNearby('position_list.txt')
searchInContext = SearchInContext('unit_list.txt')


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
    
    def test_SearchInContext_g(self):
        context = """
        壹、公訴意旨略以：
        一、被告黃望修於民國96年間擔任上市公司陽明海運股份有限公
            司（為股票公開發行、上市之公司，股票代號：2609，下稱
            : 陽明海運公司）董事長；被告石溪岸於96年間係陽明海運
            公司事業開發部副協理兼事業開發組經理，分別為陽明海運
            公司之董事、經理人及受僱人。依據行政院金融監督管理委
            員會（下稱行政院金管會）所定「公開發行公司取得或處分
            資產處理準則」第9 條之規定，以及「陽明海運公司取得或
            處分資產處理程序」第8 條之規定，陽明海運公司取得或處
            分不動產或其他固定資產交易金額達公司實收資本額百分之
            二十或新臺幣（下同）3 億元以上者，應先取得專業估價者
            出具之估價報告，交易金額達10億元以上者，應請2 家以上
            之專業估價者估價，若2 家以上專業估價者之估價結果差距
            達交易金額百分之10以上者，應洽請會計師依會計研究發展
            基金會所發布之審計準則公報第20號規定辦理，並對差異原
            因及交易價格之允當性表示具體意見。是以，屬公開發行、
            上市公司之陽明海運公司，關於資產取得或處分，自應依前
            開「公開發行公司取得或處分資產處理準則」、「陽明海運
            公司取得或處分資產處理程序」之相關營業常規辦理。
        """
        context = context.replace("\n","").replace(" ","")
        # print(context)
        new_tag = searchInContext.run(context=context,tag='陽明海運公司',bound=50,max_look_ahead=30,max_look_back=30)
        self.assertEqual(new_tag,"陽明海運股份有限公司")  
    
    def test_SearchInContext_h(self):
        context = """
        一、陳鳳廷與吳榮仁接洽承接「榮仁實業有限公司」（址原設臺
        北市○○區○○路442號7樓之4，後改設臺北縣新莊市[現改
        制為新北市新莊區○○○路351號1樓，下稱「榮仁公司」）
        後，明知林盈烜（涉嫌違反商業會計法、稅捐稽徵法等案件
        ，業經臺灣板橋地方法院檢察署檢察官認為與本院97年度易
        字第4621號判決之犯罪行為，係屬連續犯裁判上一罪關係
        """
        context = context.replace("\n","").replace(" ","")
        new_tag = searchInContext.run(context=context,tag='榮仁公司',bound=50,max_look_ahead=100,max_look_back=50)
        self.assertEqual(new_tag,"榮仁實業有限公司")  

if __name__ == '__main__':
    unittest.main()

