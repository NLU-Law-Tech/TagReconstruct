# TagReconstruct
依據字典重建標記結果；原始流程選取機率最高作為輸出，並且過濾不合理輸出，然而不能保證輸出符合正規劃期望。
## 策略
### SearchNearby
依照位置擴大搜尋可能的邊界範圍，不可以處理跨段
> 適用：身份、職稱
```python
context = """
王小明是公司實際負責人
"""
search = SearchNearby('position_list.txt')
new_tag = search.run(context=context,start_at=9,end_at=12,bound=3)
print(context[9:12],new_tag) # 負責人, 實際負責人
```

### SearchInContext
依照提示在內文中搜尋，可以處理跨段
> 適用：單位
```python
context = """
炎隆鐵工廠有限公司下稱炎隆
"""
search = SearchInContext('company_list.txt')
new_tag = search.run(context=context,tag='炎隆',bound=10)
print(new_tag) # 炎隆鐵工廠有限公司
```
