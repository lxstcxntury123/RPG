import random
import time

class PersonagemBase:
    def __init__(self, nome, classe, hp, atk):
        self.nome = nome
        self.classe = classe
        self.hp = hp
        self.atk = atk
        self.inv = []

    def status(self):
