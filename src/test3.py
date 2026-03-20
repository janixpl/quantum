import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def entanglement_with_phase():
    qml.Hadamard(wires=0)
    qml.PauliZ(wires=0)  # Dodajemy obrót fazy
    qml.CNOT(wires=[0, 1])
    return qml.state()

state = entanglement_with_phase()
print("Stan splątany (Stan Bella):")
print(state)
print("\nPrawdopodobieństwa:")
print(np.abs(state)**2)