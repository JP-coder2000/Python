pesos = int(input('How much money you have in pesos? '))
soles = int(input('How much money you have in soles? '))
reais = int(input('How much money you have in reis? '))

pesos_to_usd = pesos * 0.00025
soles_to_usd = soles * 0.27
reais_to_usd = reais * 0.20

total_dollar_amount = pesos_to_usd + soles_to_usd + reais_to_usd
print(total_dollar_amount)