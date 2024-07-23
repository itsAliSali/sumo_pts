import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


data_X = np.load('input.npy')
data_y = np.load('output.npy').reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size=0.2, 
                                                    random_state=37)

scaler = MinMaxScaler()
y_train_s = scaler.fit_transform(y_train)
y_test_s = scaler.transform(y_test)


model = MLPRegressor(hidden_layer_sizes=[20, 20],
                     random_state=1,
                     activation='relu',
                     learning_rate_init=0.1,
                     solver='sgd',
                     tol=1e-10,
                     alpha=0.1,
                     max_iter=1000).fit(X_train, y_train_s.reshape(-1))

y_train_predicted = model.predict(X_train)
y_test_predicted = model.predict(X_test)

print(f'RMSE: train= {mean_squared_error(y_train_s, y_train_predicted)}, test= {mean_squared_error(y_test_s, y_test_predicted)}')
print(f'R2 score: train= {r2_score(y_train_s, y_train_predicted)}, test= {r2_score(y_test_s, y_test_predicted)}')

plt.plot(model.loss_curve_)
plt.xlabel('# epoch')
plt.ylabel('RMSE(train set)')
plt.yscale('log')
plt.title('Leaning curve')
plt.grid(True)
plt.savefig('learningC.png', dpi=550)
plt.show()
