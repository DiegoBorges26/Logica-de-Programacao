numeroPositivo = 0
numeroNegativo = 0
for numero in range(1,11):
    numeroSolicitado = float(input("Digite o numero:"))
    if numeroSolicitado > 0:
        numeroPositivo +=1
    else: 
        numeroNegativo +=1

print(f"Numero postivos: {numeroPositivo}")
print(f"Numeoro negativos: {numeroNegativo}")

