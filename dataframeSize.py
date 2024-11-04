# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:06:16 2024

@author: andre
"""
from typing import List
import pandas as pd

def getDataframeSize(players: pd.DataFrame, columns: List[str] = None) -> List:
    # Cria o DataFrame usando a biblioteca pandas
    players = pd.DataFrame(players, columns=columns)
    return [players.shape[0], players.shape[1]]


# Testando a função
players = [
    [1, 85, 90],
    [2, 78, 88],
    [3, 92, 95]
]
# Atribuindo nomes às colunas
columns = ["ID", "Math", "Science"]

# Chamando a função e imprimindo o resultado
players = getDataframeSize(players, columns=columns)
print(players)
