import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# df = pd.DataFrame({"from": ["r_dd_recsys_item_simitem_ad_total", "r_dd_recsys_ad_type_item_rank", "r_dd_recsys_high_uv_item"],
#               "to": ["r_dd_recsys_sim_ad_new_ctr_rodes", "r_dd_recsys_sim_ad_new_ctr_rodes", "r_dd_recsys_sim_ad_new_ctr_rodes"]})
#
# df1 = pd.DataFrame({"from": ["r_dd_recsys_item_simitem_ad_base_vector", "r_dd_recsys_item_2_ad_item"],
#               "to": ["r_dd_recsys_item_simitem_ad_total", "r_dd_recsys_item_simitem_ad_total"]})
#
# df2 = pd.DataFrame({"from": ["r_dd_recsys_qualify_item", "r_dd_recsys_ad_acp", "r_dd_recsys_ad_seller_info_hour_new"],
#                     "to": ["r_dd_recsys_ad_type_item_rank", "r_dd_recsys_ad_type_item_rank", "r_dd_recsys_ad_type_item_rank"]})
#
# df3 = pd.DataFrame({"from": ["r_di_recsys_user_item_graph"],
#                     "to": ["r_dd_recsys_high_uv_item"]})

df = pd.DataFrame({"from": ["item_simitem_ad_total", "ad_type_item_rank", "high_uv_item"],
              "to": ["sim_ad_new_ctr_rodes", "sim_ad_new_ctr_rodes", "sim_ad_new_ctr_rodes"]})

df1 = pd.DataFrame({"from": ["item_simitem_ad_base_vector", "item_2_ad_item"],
              "to": ["item_simitem_ad_total", "item_simitem_ad_total"]})

df2 = pd.DataFrame({"from": ["qualify_item", "ad_acp", "ad_seller_info_hour_new"],
                    "to": ["ad_type_item_rank", "ad_type_item_rank", "ad_type_item_rank"]})

df3 = pd.DataFrame({"from": ["user_item_graph"],
                    "to": ["high_uv_item"]})


total = pd.concat([df, df1])
print(total)

G = nx.from_pandas_edgelist(total, 'from', 'to', create_using=nx.DiGraph())

nx.draw(G, with_labels=True, node_color="skyblue", font_size =7, pos=nx.circular_layout(G))

plt.savefig("table_dependency.png")
plt.show()
