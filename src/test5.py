import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def swap_bell_states():
    # 1. Tworzymy Phi+
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    
    # 2. Jednym ruchem zmieniamy go w Phi-
    qml.PauliZ(wires=0) 
    
    return qml.state()

state = swap_bell_states()
print("Nowy stan (powinieneś widzieć minusa na końcu):")
print(state)

print("\nPrawdopodobieństwa:")
print(np.abs(state)**2)