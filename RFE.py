import pandas as pd 

import time
start_time = time.time()


data_path = r'2019_2020_TB_ERA5_full_11.csv'
njobs = 20
target_type = 'cls' 
random_state = 42

# -------------------------

data = pd.read_csv(data_path)
data['classification'] = 0
data.loc[data['value']> 0, 'classification'] = 1

# -------------------------

if target_type == 'reg':
    target = 'value'
    rank_fname = f'{target_type}_FRE.xlsx'
elif target_type == 'cls':
    target = 'classification'
    rank_fname = f'{target_type}_FRE.xlsx'

# -------------------------
labels = data.drop(['utc_time', 'x_id', 'y_id', 'value', 'CIN'], axis=1).columns.tolist()
X = data[labels]
y = data[target]
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import RFE
if target_type == 'reg':
    model = RandomForestRegressor(max_depth=8, random_state= random_state, n_jobs=njobs)
elif target_type == 'cls':
    model = RandomForestClassifier(max_depth=8, random_state= random_state, n_jobs=njobs)

selector = RFE(model, n_features_to_select= 20, step=1)

selector = selector.fit(X, y)


features = [[x] for x in labels]
df = pd.DataFrame(features, columns=['Features'])
col_name = f'{target_type}_RFE_rank'
df[f'RFE{target_type}_rank'] = selector.ranking_
df.to_excel(rank_fname, index=False)


print("--- %s seconds ---" % (time.time() - start_time))

