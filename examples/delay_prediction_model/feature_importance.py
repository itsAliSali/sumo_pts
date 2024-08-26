import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

from sumo_pts.map.city import City


aachen = City('osm.net.xml', 'osm_pt.rou.xml')

street_names = ['Pontwall', 'Seffenter Weg', 'Forckenbeckstraße', 'Halifaxstraße',
               'Alexianergraben', 'Franzstraße', 'Jakobstraße', 'Vaalser Straße',
               'Komphausbadstraße', 'Peterstraße', 'Heinrichsallee', 'Theaterstraße',
               'Saarstraße', 'Boxgraben', 'Roermonder Straße', 'Hirschgraben']

bus_freq = aachen.show_statistics(street_names)

data_X = np.load('input.npy')
data_y = np.load('output.npy').reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size=0.2, 
                                                    random_state=37)

scaler = MinMaxScaler()
y_train_s = scaler.fit_transform(y_train)
y_test_s = scaler.transform(y_test)


model = LinearRegression()
model.fit(X_train, y_train_s)
importance = np.abs(model.coef_[0])
for i,v in enumerate(importance):
    print('Feature: %0d, Score: %.5f' % (i,v))

bar = plt.bar([x for x in range(len(importance))], importance)
bus_freq['Halifaxstraße'] = 14
for i, rect in enumerate(bar):
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, str(bus_freq[street_names[i]]), ha='center', va='bottom')

plt.xticks([x for x in range(len(importance))], street_names, rotation=90)
plt.ylabel('Regression coefficient')
plt.show()

from sklearn.ensemble import RandomForestRegressor

feature_names = [f"feature {i}" for i in range(X_train.shape[1])]
forest = RandomForestRegressor(random_state=0)
forest.fit(X_train, y_train_s.ravel())

importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)

import pandas as pd

forest_importances = pd.Series(importances, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=std, ax=ax)
ax.set_title("Feature importances using MDI")
ax.set_ylabel("Mean decrease in impurity")
fig.tight_layout()
