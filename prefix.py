""" Calculadora infix

Funcionamento
[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9
"""

__version__ = "0.1.0"

import sys

operations = (
    "sum",
    "sub",
    "mul",
    "div",
)
arguments = sys.argv[1:]

# TODO: Usar Exceptions
if not arguments:
    operation = input("Operação: ")
    n1 = input("Numero 1: ")
    n2 = input("Numero 2: ")
    arguments = [operation, n1, n2]

elif len(arguments) != 3:
    print("Numero de argumentos invalidos!")
    print("Ex: sum 5 5")
    sys.exit(1)  # passar 0 para sucesso e 1 para falha

operacao, *nums = arguments

if operacao not in operations:
    print(f"Invalid option `{operacao}`")
    sys.exit(1)


validated_nums = []
for num in nums:
    # TODO: Usar um while com Exceptions
    if not num.replace(".", "").isdigit():
        print(f"Numero inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)


n1, n2 = validated_nums

# TODO: Usar fict de funções
if operacao == "sum":
    resultado = n1 + n2
elif operacao == "sub":
    resultado = n1 - n2
elif operacao == "mul":
    resultado = n1 * n2
elif operacao == "div":
    resultado = n1 / n2

print(f"Resultado: {resultado}")
