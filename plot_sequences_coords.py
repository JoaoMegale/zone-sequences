"""
arquivo de entrada: df das sequencias gerado por sequences.py

plota as sequencias

"""

import pandas as pd
from mplsoccer import Pitch
import matplotlib.pyplot as plt

df_actions = pd.read_csv(r"C:\Users\joaom\Documents\IC\codes\final\df_actions.csv")
df_sequences = pd.read_csv(r"C:\Users\joaom\Documents\IC\codes\final\df_sequences.csv")


# escolhe a sequencia a ser plotada (numero da sequencia)
sequencia_plotada = 0
df_plotado = df_actions[df_actions['num_seq'] == sequencia_plotada]

# plot das sequencias

pitch = Pitch(pitch_type='uefa', pitch_length=105, pitch_width=68)
fig, ax = pitch.draw(figsize=(10, 7))
colors = ['blue', 'red', 'green']

X = [20, 36.25, 52.5, 68.75, 85]
Y = [14, 25, 43, 54]
for x in X:
    linha = plt.axvline(x, 0, 1, linestyle="--", color='lightgray')
    ax.add_line(linha)
for y in Y:
    if y in [25, 43]:
        linha = plt.axhline(y, 0.21, 1, linestyle="--", color='lightgray')
        ax.add_line(linha)
    else:
        linha = plt.axhline(y, 0, 1, linestyle="--", color='lightgray')
        ax.add_line(linha)
        
for i in range(1, len(df_plotado)):
    x = df_plotado['start_x'][i-1]
    y = df_plotado['start_y'][i-1]
    dx = df_plotado['start_x'][i] - x
    dy = df_plotado['start_y'][i] - y
    arrow = plt.Arrow(x, y, dx, dy, width=1, color='blue')
    ax.add_patch(arrow)
        
plt.show()
