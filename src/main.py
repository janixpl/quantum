import pennylane as qml

# Zwiększamy liczbę kubitów (wires) do 3
dev = qml.device("default.qubit", wires=3)

@qml.qnode(dev)
def my_circuit():
    # KROK 1: Robimy superpozycję na kubicie nr 0
    qml.Hadamard(wires=0)
    
    # KROK 2: Splątujemy kubit 0 z kubitem 1
    qml.CNOT(wires=[0, 1])
    
    # KROK 3: Splątujemy kubit 1 z kubitem 2 (nowość!)
    qml.CNOT(wires=[1, 2])
    
    return qml.probs(wires=[0, 1, 2])

# Rysujemy schemat adresacji
print("Schemat obwodu (Adresy 0, 1, 2):")
print(qml.draw(my_circuit)())

# Wyświetlamy wektor prawdopodobieństwa
print("\nRozkład prawdopodobieństwa (8 adresów binarnych):")
print(my_circuit())