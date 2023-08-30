# Docstring para fazer documentação
"""
Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe
a mensagem correspondende.

Como usar:
Tenha a variavel LANG devidamente configurada ex:
    export LANG=pt_BR
Ou informe atraves do CLI argument `--lang`

Ou o usuário terá que digitar

Execução
    python3 hello.py
    ou
    ./hello.py
"""
# Dunder
__version__ = "0.1.3"
__author__ = "Matheus"
__license__ = "Unlicense"

import os
import sys


# Pegar argumentos pelo CLI
# ex: python helloy.py --lang=fr_fr
# print(f"{sys.argv=}")

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    # TODO: tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    # TODO: Usar repetição
    if current_language is None:
        current_language = input("Choose a language: ")
current_language = current_language[:5]
# snake_case
# sets (Hash table) - O(1) - constante

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mundo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language] * int(arguments["count"]))


# Order de Complexidade O(n)
# if current_language == "pt_BR":
#     msg = "Olá, mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "es_EP":
#     msg = "Hola, Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour Monde"


# print(msg)
