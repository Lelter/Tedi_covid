#%%

import pandas as pd


def leijia(x):
    x["累计确诊"] = x['新增确诊'].cumsum()
    x["累计治愈"] = x['新增治愈'].cumsum()
    x["累计死亡"] = x['新增死亡'].cumsum()
    return x
    pass


path = "附件1.xlsx"

data = pd.read_excel(path)
data = data.groupby("城市")
data = data.apply(leijia)
data.to_csv("result/task1_1.csv", index=False)
datatemp = data.groupby("城市")
data_wuhan = datatemp.get_group("武汉")
data_shenzhen = datatemp.get_group("深圳")
data_baoding = datatemp.get_group("保定")
data_wuhan = pd.DataFrame(data_wuhan)
data_shenzhen = pd.DataFrame(data_shenzhen)
data_baoding = pd.DataFrame(data_baoding)
data_wuhan_result = data_wuhan[(data_wuhan["日期"].dt.day == 10)].append(data_wuhan[(data_wuhan["日期"].dt.day == 25)])
data_shenzhen_result = data_shenzhen[(data_shenzhen["日期"].dt.day == 10)].append(
    data_shenzhen[(data_shenzhen["日期"].dt.day == 25)])
data_baoding_result = data_baoding[(data_baoding["日期"].dt.day == 10)].append(
    data_baoding[(data_baoding["日期"].dt.day == 25)])
task_1_1 = data_wuhan_result.append(data_shenzhen_result)
task_1_1 = task_1_1.append(data_baoding_result)
task_1_1.to_csv("temp/task1.csv", encoding="utf_8_sig")



#%%
data.info()
shengfen = pd.read_excel("附件1.xlsx", sheet_name="城市省份对照表")
result = pd.DataFrame(columns=['日期', '省份', '新增确诊'])
# '新增治愈', '新增死亡', '累计确诊', '累计治愈', '累计死亡']
# for row in data.iterrows()
#%%
count=0
for d in data.iterrows():
    for s in shengfen.iterrows():
        if d[1]["城市"] == s[1]["城市"]:
            print(d[1]["城市"],s[1]["省份"],count)
            d[1]["城市"] = s[1]["省份"]
            count=count+1

print(data)