#! /usr/bin/python3
"""Hello World Multi Línguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR
Execução:

    python4 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Bruno Rocha"
__license__ = "Unlicense"

current_language = "en_US"

msg = "Hello, World!"

if current_language = "pt_BR":
    msg = "Olá Mundo!"
elif current_language = "it_IT"
    msg = "Ciao Mondo!"

print(msg)