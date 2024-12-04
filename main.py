import os
import argparse
from banco_de_dados import gerar_dados
from treinamento_modelo import treinar_modelo
from comparacao_saidas import comparar_saidas

def arquivos_existem():
    return os.path.exists("X.npy") and os.path.exists("y.npy") and os.path.exists("modelo_treinado.pkl") and os.path.exists("scaler.pkl")

def main(regenerate=False):
    if regenerate or not arquivos_existem():
        if regenerate:
            print("Opção 'regenerate' ativada. Gerando novos dados e treinando modelo...")
        else:
            print("Arquivos necessários não encontrados. Gerando dados e treinando modelo...")
        gerar_dados()
        treinar_modelo()
        print("Dados e modelo gerados com sucesso!")
    else:
        print("Arquivos encontrados. Pulando geração de dados e treinamento.")

    mse = comparar_saidas()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--regenerate',
        action='store_true'
    )
    args = parser.parse_args()
    main(regenerate=args.regenerate)
