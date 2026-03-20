import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def different_qubits_circuit():
    qml.PauliX(wires=1)    # Ustawiamy drugi kubit na |1>
    qml.Hadamard(wires=0)  # Pierwszy w superpozycji
    qml.CNOT(wires=[0, 1]) # Splątanie
    return qml.state()

state = different_qubits_circuit()
print("Stan splątany (Stan Bella):")
print(state)
print("\nPrawdopodobieństwa:")
print(np.abs(state)**2)