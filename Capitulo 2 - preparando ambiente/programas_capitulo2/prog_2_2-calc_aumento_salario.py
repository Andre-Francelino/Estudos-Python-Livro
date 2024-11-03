# Programa 2.2 - Cálculo de aumento de salário

# guardando o valor de 1500 na variável salário
salario = 1500
# guardando o valor de 5 na variável aumento (esse valor equivale ao aumento em 5%)
aumento = 5
# usando a função print para exibir valor calculado. 
# a operação entre parênteses será executada primeiro.
# dentro do parênteses a divisão de aumento/100 tem maior prioridade, 
# para depois o resultado multiplicar com o salário, para só por ultimo somar com o salário fora dos parênteses
print(salario + (salario * aumento / 100))
