import numpy as np
import joblib
from sklearn.metrics import mean_squared_error

def comparar_saidas():
    # Carregar os dados
    X = np.load('X.npy')
    y = np.load('y.npy')

    # Carregar modelo e scaler
    modelo = joblib.load('modelo_treinado.pkl')
    scaler = joblib.load('scaler.pkl')

    # Escalar os dados
    X_scaled = scaler.transform(X)

    # Fazer previsões
    y_pred = modelo.predict(X_scaled)

    # Calcular erro médio quadrático
    mse = mean_squared_error(y, y_pred)
    print(f"Mean Squared Error (MSE): {mse}")
    return mse

if __name__ == "__main__":
    comparar_saidas()
