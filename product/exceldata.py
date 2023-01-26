import pandas as pd
from .models import Product

dfs = pd.read_excel(r'E:\kiran\orackel\static\data.xlsx')
print(dfs.columns)
for i in dfs.index:
    d = dfs['Description'][i]

    p = Product(name=dfs['Report Title'][i], description=d.splitlines()[0], category=dfs['Category'][i],
                table_of_Content=dfs['Table of Contents'][i], additional=d, single_user=dfs['SINGLE USER'][i],
                multi_user=dfs['MULTIPLE / CORPORATE'][i], cooperate_user=dfs['MULTIPLE / CORPORATE'][i],data_pack=dfs['DATA PACK'][i])
    p.save()
