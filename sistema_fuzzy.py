import numpy as np
import skfuzzy as fuzz
from skfuzzy.control import Antecedent, Consequent, Rule, ControlSystem, ControlSystemSimulation

# Definição das variáveis fuzzy
aparencia = Antecedent(np.arange(0, 21, 1), 'aparencia')
ph = Antecedent(np.arange(0, 14.1, 0.1), 'ph')
turbidez = Antecedent(np.arange(0, 11, 1), 'turbidez')
qualidade = Consequent(np.arange(0, 101, 1), 'qualidade')

# Funções de pertinência para Aparência
aparencia['boa'] = fuzz.trimf(aparencia.universe, [0, 0, 10])
aparencia['adequada'] = fuzz.trimf(aparencia.universe, [5, 10, 15])
aparencia['inadequada'] = fuzz.trimf(aparencia.universe, [10, 20, 20])

# Funções de pertinência para pH
ph['inadequado baixo'] = fuzz.trimf(ph.universe, [0, 0, 6])
ph['adequado baixo'] = fuzz.trimf(ph.universe, [5, 7, 8])
ph['bom'] = fuzz.trimf(ph.universe, [7, 8, 9])
ph['adequado alto'] = fuzz.trimf(ph.universe, [8, 10, 12])
ph['inadequado alto'] = fuzz.trimf(ph.universe, [10, 14, 14])

# Funções de pertinência para Turbidez
turbidez['adequada'] = fuzz.trimf(turbidez.universe, [0, 0, 5])
turbidez['media'] = fuzz.trimf(turbidez.universe, [3, 5, 7])
turbidez['alta'] = fuzz.trimf(turbidez.universe, [5, 10, 10])

# Funções de pertinência para Qualidade
qualidade['inadequada'] = fuzz.trimf(qualidade.universe, [0, 0, 50])
qualidade['adequada'] = fuzz.trimf(qualidade.universe, [25, 50, 75])
qualidade['boa'] = fuzz.trimf(qualidade.universe, [50, 100, 100])

# Definição das regras
regras = [
    Rule(aparencia['boa'] & ph['bom'] & turbidez['adequada'], qualidade['boa']),
    Rule(aparencia['adequada'] & ph['bom'] & turbidez['adequada'], qualidade['adequada']),
    Rule(aparencia['inadequada'] | ph['inadequado baixo'] | ph['inadequado alto'], qualidade['inadequada']),
    Rule(turbidez['alta'], qualidade['inadequada']),
    Rule(ph['adequado baixo'] & turbidez['media'], qualidade['adequada']),
]

# Adicionar mais regras para cobrir todos os casos possíveis
regras.extend([
    Rule(aparencia['boa'] & ph['adequado baixo'] & turbidez['adequada'], qualidade['adequada']),
    Rule(aparencia['adequada'] & ph['bom'] & turbidez['media'], qualidade['adequada']),
    Rule(aparencia['inadequada'] & ph['adequado alto'], qualidade['inadequada']),
    Rule(ph['adequado alto'] & turbidez['alta'], qualidade['inadequada']),
    Rule(aparencia['boa'] & ph['bom'] & turbidez['alta'], qualidade['adequada']),
])

# Sistema de controle
sistema = ControlSystem(regras)
simulador = ControlSystemSimulation(sistema)
