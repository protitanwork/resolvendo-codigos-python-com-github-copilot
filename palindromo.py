

print("=== Verificador de Palíndromos ===\n")

# Entrada do usuário
palavra = input("Digite uma palavra: ")

# Inversão da string usando slicing
palavra_invertida = palavra[::-1]

# Verificação
if palavra == palavra_invertida:
    print(f"\nA palavra '{palavra}' é um PALÍNDROMO.")
else:
    print(f"\nA palavra '{palavra}' NÃO é um palíndromo.")
