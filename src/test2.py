import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def entanglement_circuit():
    qml.Hadamard(wires=0) # Pierwszy kubit w superpozycji
    qml.CNOT(wires=[0, 1]) # "Sklejamy" je ze sobą
    return qml.state()

state = entanglement_circuit()
print("Stan splątany (Stan Bella):")
print(state)
print("\nPrawdopodobieństwa:")
print(np.abs(state)**2)