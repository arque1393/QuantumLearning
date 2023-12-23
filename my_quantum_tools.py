import qiskit as qk 
def numeric_state_set( N:int=1 ):
    N = bin(N)[2:]; n = len(N)
    qc = qk.QuantumCircuit(n)
    qc.x([n-i-1 for i,e in enumerate(N)  if int(e) ])
    return qc 