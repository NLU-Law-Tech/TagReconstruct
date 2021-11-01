# TagReconstruct
依據字典重建標記結果，使得輸出符合正規期望

## 內建清單
首次初始化會下載一些內建清單，也可自己指定
- `unit_list.txt`(公司+公部門，每月更新)
- `company_list.txt`
- `identity_list.txt`
- `position_list.txt`

## 安裝
```
pip install -U git+https://github.com/NLU-Law-Tech/TagReconstruct.git
```

## 策略
### SearchNearby
依照位置擴大搜尋可能的邊界範圍，不可以處理跨段
> 適用：身份、職稱
```python
searchNearby = SearchNearby('position_list.txt')
context = "王小明是公司實際負責人"
new_tag = searchNearby.run(context=context,start_at=9,end_at=12,bound=3)
# 實際負責人
```

### SearchInContext
依照提示在內文中搜尋，可以處理跨段
> 適用：單位
```python
searchInContext = SearchInContext('company_list.txt')
context = "炎隆鐵工廠有限公司下稱炎隆"
new_tag = searchInContext.run(context=context,tag='炎隆',bound=10)
# 炎隆鐵工廠有限公司     

context = "華新行實業股份有限公司下稱華實公司"
new_tag = searchInContext.run(context=context,tag='華實公司',bound=10)
# 華新行實業股份有限公司
```
