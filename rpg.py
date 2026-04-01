python
import random  # 1. Biblioteca para rolagens de dados (D20, dano, etc)
import time    # 2. Para dar pausas dramáticas no texto

class PersonagemBase: # 3. Definição da classe (sem parênteses se não houver herança)
    def __init__(self, nome, classe, hp, atk): # 4. O "Constructor". O 'self' é o 'this' do Java
        self.nome = nome     # 5. Atributo Nome
        self.classe = classe # 6. Atributo Classe
        self.hp = hp         # 7. Pontos de Vida
        self.atk = atk       # 8. Poder de Ataque
        self.inv = []        # 9. Inventário (uma lista dinâmica, como ArrayList)

    def status(self):        # 10. Um método simples para checar o herói
