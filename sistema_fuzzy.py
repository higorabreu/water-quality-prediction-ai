import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definição das entradas
aparencia = ctrl.Antecedent(universe=(0, 20), label='aparencia')
ph = ctrl.Antecedent(universe=(0, 14), label='ph')
turbidez = ctrl.Antecedent(universe=(0, 10), label='turbidez')

# Definição da saída
qualidade = ctrl.Consequent(universe=(0, 100), label='qualidade')

# Regras fuzzy
aparencia.automf(3)
ph.automf(3)
turbidez.automf(3)

qualidade['ruim'] = fuzz.trimf(qualidade.universe, [0, 0, 50])
qualidade['média'] = fuzz.trimf(qualidade.universe, [25, 50, 75])
qualidade['boa'] = fuzz.trimf(qualidade.universe, [50, 100, 100])

rule1 = ctrl.Rule(aparencia['poor'] | ph['poor'] | turbidez['poor'], qualidade['ruim'])
rule2 = ctrl.Rule(aparencia['average'] & ph['average'] & turbidez['average'], qualidade['média'])
rule3 = ctrl.Rule(aparencia['good'] & ph['good'] & turbidez['good'], qualidade['boa'])

# Sistema de controle
control = ctrl.ControlSystem([rule1, rule2, rule3])
simulador = ctrl.ControlSystemSimulation(control)
