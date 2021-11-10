# %%

import pandas as pd

path = "附件1.xlsx"

data = pd.read_excel(path)

data = data.groupby("城市")


def leijia(x):
    x["累计确诊"] = x['新增确诊'].cumsum()
    x["累计治愈"] = x['新增治愈'].cumsum()
    x["累计死亡"] = x['新增死亡'].cumsum()
    return x
    pass


data = data.apply(leijia)

data.to_csv("result/1_1.csv")

# %%

data = data.groupby("城市")
data_wuhan = data.get_group("武汉")
data_shenzhen = data.get_group("深圳")
data_baoding = data.get_group("保定")

data_wuhan.loc(data_wuhan["日期"].str.contains("25"))
