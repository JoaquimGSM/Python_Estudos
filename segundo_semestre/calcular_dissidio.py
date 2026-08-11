def calcular_dissidio(salario: float, percentual: float = 0.08) -> float:
    if percentual >= 1:
        percentual /= 100

    salario_aumento = salario * (1 + percentual)
    return salario_aumento


# O parametro default é aquele valor que é definido na funcao para quando
# nao quisermos passar o valor
salario_atual = 10000

print(
    f'Com o dissidio o seu salario passou de R${salario_atual} para '
    f'R${calcular_dissidio(salario=salario_atual, percentual=0.5)}'
)



# O parametro default é aquele valor que é definido na funcao para quando
# nao quisermos passar o valor
salario_atual = 10000

# Passando parametro do percentual de aumento
print(
    f'Com o dissidio o seu salario passou de R${salario_atual:.2f} para '
    f'R${calcular_dissidio(salario=salario_atual, percentual=0.5):.2f}'
)

# Nao passa o percentual de aumento e usa o valor default
print(
    f'Com o dissidio o seu salario passou de R${salario_atual:.2f} para '
    f'R${calcular_dissidio(salario=salario_atual):.2f}'
)