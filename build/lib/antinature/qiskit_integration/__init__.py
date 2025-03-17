"""
Qiskit integration module for antinature quantum chemistry.

This module provides integration with Qiskit and Qiskit-Nature
for simulating antinature systems on quantum computers.
"""

# Check if Qiskit is available
try:
    import qiskit
    import qiskit_nature
    from qiskit_algorithms import VQE, NumPyMinimumEigensolver
    from qiskit_algorithms.optimizers import COBYLA, SPSA
    from qiskit.primitives import Estimator
    HAS_QISKIT = True
except ImportError:
    HAS_QISKIT = False
    print("Warning: Qiskit or dependent packages not available. Qiskit integration will be disabled.")

# Always import the modules, but the classes will raise an error if Qiskit is not available
from .adapter import QiskitNatureAdapter
from .circuits import AntinatureCircuits, PositroniumCircuit
from .solver import PositroniumVQESolver
from .systems import AntinatureQuantumSystems
from .antinature_solver import AntinatureQuantumSolver
from .vqe_solver import AntinatureVQESolver
from .ansatze import AntinatureAnsatz

# Define what should be exposed at package level
__all__ = [
    'QiskitNatureAdapter',
    'antinatureCircuits',
    'PositroniumCircuit',
    'PositroniumVQESolver',
    'antinatureQuantumSystems',
    'antinatureQuantumSolver',
    'antinatureVQESolver',
    'antinatureAnsatz',
    'HAS_QISKIT'
]