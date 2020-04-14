import pandas as pd
from pyecharts.charts import Sankey
from pyecharts import options as opts

df = pd.DataFrame({
    "性别": ['男', '男', '男', '女', '女', '女'],
    "熬夜原因": ['打游戏', '加班', '看剧', '打游戏', '加班', '看剧'],
    "人数": [57, 13, 30, 33, 5, 62]
})

print(df)

nodes = []

for i in range(2):
    values = df.iloc[:, i].unique()
    for value in values:
        dic = {}
        dic['name'] = value
        nodes.append(dic)

print(nodes)

links = []

for i in df.values:
    dic = {}
    # source, target, value
    dic['source'] = i[0]
    dic['target'] = i[1]
    dic['value'] = i[2]
    links.append(dic)

print(links)

pic = (
    Sankey()
    .add('',
         nodes,
         links,
         linestyle_opt=opts.LineStyleOpts(opacity=0.3, curve=0.5, color = "source"),
         label_opts=opts.LabelOpts(position="right"),
         node_gap = 30,
    ).set_global_opts(title_opts=opts.TitleOpts(title = '熬夜原因桑基图'))
)
pic.render('sankey.html')






