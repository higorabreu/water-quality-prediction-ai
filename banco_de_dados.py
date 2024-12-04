import numpy as np
from sistema_fuzzy import simulador

def gerar_dados():
    # Gerar entradas (aparência, pH, turbidez)
    aparencias = np.linspace(0, 20, 10)
    phs = np.linspace(0, 14, 10)
    turbidezes = np.linspace(0, 10, 10)

    X = []
    y = []

    # Gerar dados do sistema fuzzy
    for aparencia in aparencias:
        for ph in phs:
            for turbidez in turbidezes:
                try:
                    simulador.input['aparencia'] = aparencia
                    simulador.input['ph'] = ph
                    simulador.input['turbidez'] = turbidez
                    simulador.compute()
                    qualidade = simulador.output['qualidade']

                    X.append([aparencia, ph, turbidez])
                    y.append(qualidade)
                except Exception as e:
                    print(f"Erro ao calcular. Entrada: Aparência={aparencia}, pH={ph}, Turbidez={turbidez}. Erro: {e}")

    # Salvar os dados como arrays numpy
    np.save('X.npy', np.array(X))
    np.save('y.npy', np.array(y))


if __name__ == "__main__":
    gerar_dados()