# Stonks 📈
# Codédex

stock_prices = [ 6.15, 5.81, 5.70, 5.65, 5.33, 5.62, 5.19, 6.13, 7.20, 7.34, 7.95, 7.53, 7.39, 7.59, 7.27 ]


#lo que estamos haciendo es pasandole que valor queremos que nos muestre 
#(i es la posicion que queremos)

def price_at(i):
  return stock_prices[i-1]

#esta parte es confusa, pero lo primero que hace es recibir de que indice a que indice
#va a recorrer la lista, eso lo pasamos como parametro (a,b)
#despues inicializamos el valor maximo en 0
#despues recorremos toda la lista pero miesntras lo hacemos vamos comparando
#el valor actual de max con el valor del indice en el que actualmente va el ciclo for
#hace la comparación y regresa a la variable el mas grande
def max_price(a, b):
  mx = 0
  for i in range(a, b + 1):
    mx = max(mx, price_at(i))
  return mx

def min_price(a, b):
  mn = price_at(a)
  for i in range(a, b + 1):
    mn = min(mn, price_at(i))
  return mn

print(max_price(1, 15))
print(min_price(5, 10))
print(price_at(3))