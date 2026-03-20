import pennylane as qml
import matplotlib.pyplot as plt
from qutip import Bloch, Qobj # Dodajemy import Qobj
import numpy as np

dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def circuit(theta, phi):
    qml.RX(theta, wires=0)
    qml.RY(phi, wires=0)
    return qml.state()

# Generujemy stan
state_data = circuit(1.57, 0.78) 

# KLUCZOWA POPRAWKA: Konwertujemy wynik PennyLane na Qobj z QuTip
# Musimy to zapisać jako wektor kolumnowy (2 wiersze, 1 kolumna)
state_qutip = Qobj(np.array(state_data).reshape(2, 1))

# Wizualizacja
b = Bloch()
b.add_states(state_qutip) # Teraz QuTip dostaje to, co kocha: Qobj
b.show()
plt.show()