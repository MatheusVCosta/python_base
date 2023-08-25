#Docstring para fazer documentação
"""
Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe
a mensagem correspondende.

Como usar:
Tenha a variavel LANG devidamente configurada ex:
    export LANG=pt_BR
    
Execução
    python3 hello.py
    ou
    ./hello.py
"""
#Dunder 
__version__ = "0.0.1"
__author__ = "Matheus"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
#snake_case
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_EP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde"

print(msg)