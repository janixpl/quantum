import pennylane as qml
import numpy as np

# Definiujemy urządzenie z DWOMA kubitami
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def two_qubit_circuit():
    qml.Hadamard(wires=0) # Superpozycja na pierwszym kubicie
    qml.Hadamard(wires=1) # Superpozycja na drugim kubicie
    return qml.state()

state = two_qubit_circuit()

print("Wektor stanu (4 liczby zespolone):")
print(state)

print("\nPrawdopodobieństwa (|z|^2):")
print(np.abs(state)**2)