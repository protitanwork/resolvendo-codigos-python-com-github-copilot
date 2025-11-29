

print("=== Verificação de Par ou Ímpar ===\n")

# Entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Verificação usando o operador módulo (%)
if numero % 2 == 0:
    print(f"\nO número {numero} é PAR.")
else:
    print(f"\nO número {numero} é ÍMPAR.")
