Predição da Qualidade da Água

Descrição:  
O programa prevê a qualidade da água com base nos parâmetros de aparência, pH e turbidez. Ele utiliza um sistema fuzzy para gerar dados e treina um modelo de machine learning para realizar as previsões.

Arquivos do Projeto:  
1. sistema_fuzzy.py: Define o sistema fuzzy utilizado para simular a qualidade da água.  
2. banco_de_dados.py: Gera dados de entrada e saída usando o sistema fuzzy.  
3. treinamento_modelo.py: Treina o modelo com os dados gerados.  
4. comparacao_saidas.py: Compara as previsões do modelo com os dados reais.  
5. main.py: Centraliza a execução do programa.

Bibliotecas: numpy, scikit-learn, scikit-fuzzy, argparse.  

Para instalar as dependências, use o comando:  
pip install numpy scikit-learn scikit-fuzzy

Como Executar:  
1. Primeira execução:  
   python main.py  
   Isso gera os dados, treina o modelo e compara as previsões.

2. Regerar dados e treinar modelo(força a geração de dados):  
   python main.py --regenerate  

3. Apenas comparar saídas:  
   python main.py  

Saídas do Programa:  
- Score (R²): Mede a qualidade do modelo (valores próximos de 1 indicam bom desempenho).  
- Erro Quadrático Médio (MSE): Mede a precisão das previsões (valores menores indicam maior precisão).  

Estrutura de Arquivos Gerados:  
- X.npy e y.npy: Dados de entrada e saída gerados.  
- modelo_treinado.pkl: Modelo treinado.  
- scaler.pkl: Escalador para normalizar os dados.
