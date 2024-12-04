import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
import joblib

def treinar_modelo():
    # Carregar os dados
    X = np.load('X.npy')
    y = np.load('y.npy')

    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    # Escalar os dados
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Treinar o modelo
    modelo = MLPRegressor(max_iter=3000, random_state=1)
    modelo.fit(X_train, y_train)

    # Avaliar o modelo
    score = modelo.score(X_test, y_test)
    print(f"Score (R²): {score}")

    # Salvar modelo e scaler
    joblib.dump(modelo, 'modelo_treinado.pkl')
    joblib.dump(scaler, 'scaler.pkl')

if __name__ == "__main__":
    treinar_modelo()
