import pandas as pd
shengfen = pd.read_excel("附件1.xlsx", sheet_name="城市省份对照表")
data = pd.read_csv("result/1_1.csv")
result = pd.DataFrame(columns=['日期', '省份', '新增确诊'])
# '新增治愈', '新增死亡', '累计确诊', '累计治愈', '累计死亡']
for cheng in data.itertuples():
    for sheng in shengfen.itertuples():
        # print(sheng["城市"])

        if cheng.城市 == sheng.城市:
            if result.loc(result["省份"]==result[sheng.省份]):
                dic = {"日期": cheng.日期, "省份": sheng.省份, '新增确诊': result[sheng.省份].新增确诊 + cheng.新增确诊
                       }
                result.append(dic)

print(result)