import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

# Carregar banco de dados
dados = np.loadtxt("banco_dados.csv", delimiter=",", skiprows=1)
X = dados[:, :3]  # Entradas: aparencia, ph, turbidez
y = dados[:, 3]   # Saída: qualidade

# Dividir os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar a rede neural
modelo = MLPRegressor(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
modelo.fit(X_train, y_train)

# Avaliar o modelo
y_pred = modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Erro Quadrático Médio (MSE): {mse}")
