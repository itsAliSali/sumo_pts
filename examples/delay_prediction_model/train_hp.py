import time

import numpy as np
import tensorflow as tf
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from ray import train, tune
from ray.tune.schedulers import PopulationBasedTraining


class MyCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        train.report({"val_loss": logs.get('val_loss')})


def train_model(config):
    number_epochs = 1000
    batch_size = 160

    number_layers = config['n_l']
    lr = config['lr']
    
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(X_train.shape[1]))
    
    for i in range(number_layers):
        model.add(tf.keras.layers.Dense(config[f"hidden{i+1}"], activation='sigmoid'))
    
    model.add(tf.keras.layers.Dense(y_train.shape[1]))
    
    optt = tf.keras.optimizers.Adam(learning_rate=lr)  

    model.compile(loss='mse',
                    optimizer=optt,
                    metrics=['mae'])
    
    history = model.fit(X_train, y_train_s,
                    epochs=number_epochs, batch_size=batch_size, verbose=True,
                    validation_data=(X_test, y_test_s),
                    callbacks=[MyCallback()])

    val_loss = history.history["val_loss"][-1]
    return {"val_loss": val_loss, 'model': model, 'history': history}


def tune_model():
    
    pbt = PopulationBasedTraining(
    time_attr="training_iteration",
    perturbation_interval=200,  
    hyperparam_mutations={
            "n_l": tune.choice([2, 3]),
            "lr": tune.loguniform(1e-5, 1e-1),
            "hidden1": tune.uniform(10, 100),
            "hidden2": tune.uniform(10, 100),
            "hidden3": tune.uniform(10, 100),
        },
    )

    tuner = tune.Tuner(
        train_model,
        tune_config=tune.TuneConfig(
            metric="val_loss",
            mode="min",
            scheduler=pbt,
            num_samples=50,
        ),
        run_config=train.RunConfig(
            name="my_exp1",
        )
    )
    
    t_i = time.time()
    results = tuner.fit()
    HP_fit_time = time.time() - t_i
    print('elapsed time in min: ', HP_fit_time/60)

    print("Best hyperparameters found were: ", results.get_best_result().config)
    return results


data_X = np.load('input.npy')
data_y = np.load('output.npy').reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size=0.2, 
                                                    random_state=37)

scaler = MinMaxScaler()
y_train_s = scaler.fit_transform(y_train)
y_test_s = scaler.transform(y_test)


hp_results = tune_model()
best_nn_hp = hp_results.get_best_result().config
# best_nn_hp = {'n_l': 3, 'lr': 0.008038345356318897, 'hidden1': 87.15517437945864, 'hidden2': 59.70976351699706, 'hidden3': 29.935028055960178}
# best_nn_hp = {'n_l': 3, 'lr': 0.0007038345356318897, 'hidden1': 87.15517437945864, 'hidden2': 59.70976351699706, 'hidden3': 29.935028055960178}

train_res = train_model(best_nn_hp)
model = train_res["model"]
nn_model_hist = train_res["history"]
print("\nBest hyperparameters found were: ", best_nn_hp)

plt.figure()
plt.plot(nn_model_hist.history['loss'])
plt.plot(nn_model_hist.history['val_loss'])
plt.legend(['train set', 'test set'])
plt.xlabel('# epoch')
plt.ylabel('RMS Error')
plt.yscale('log')
plt.title('Leaning curve')
plt.grid(True)
plt.savefig('learningC_HP.png', dpi=550)
plt.show()

y_train_predicted = model.predict(X_train)
y_test_predicted = model.predict(X_test)

print(f'RMSE: train= {mean_squared_error(y_train_s, y_train_predicted)}, test= {mean_squared_error(y_test_s, y_test_predicted)}')
print(f'R2 score: train= {r2_score(y_train_s, y_train_predicted)}, test= {r2_score(y_test_s, y_test_predicted)}')

