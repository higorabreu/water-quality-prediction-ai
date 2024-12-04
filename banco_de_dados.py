import sqlite3
import numpy as np
from sistema_fuzzy import simulador

# Conectar ao banco de dados
conexao = sqlite3.connect('qualidade_agua.db')
cursor = conexao.cursor()

# Criar tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS resultados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aparencia REAL,
    ph REAL,
    turbidez REAL,
    qualidade REAL
)
''')

# Gerar dados e calcular a qualidade
aparencias = np.linspace(0, 20, 5)
phs = np.linspace(0, 14, 5)
turbidezes = np.linspace(0, 10, 5)

for aparencia in aparencias:
    for ph in phs:
        for turbidez in turbidezes:
            try:
                # Inserir valores no simulador
                simulador.input['aparencia'] = aparencia
                simulador.input['ph'] = ph
                simulador.input['turbidez'] = turbidez
                simulador.compute()
                qualidade = simulador.output['qualidade']

                # Inserir resultado no banco
                cursor.execute('INSERT INTO resultados (aparencia, ph, turbidez, qualidade) VALUES (?, ?, ?, ?)', 
                               (aparencia, ph, turbidez, qualidade))
                conexao.commit()
                print(f"Salvo: Aparência={aparencia}, pH={ph}, Turbidez={turbidez}, Qualidade={qualidade}")
            except Exception as e:
                print(f"Erro ao calcular. Entrada: Aparência={aparencia}, pH={ph}, Turbidez={turbidez}. Erro: {e}")

# Fechar conexão
conexao.close()
