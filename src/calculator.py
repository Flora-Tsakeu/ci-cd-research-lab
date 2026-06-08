# src/calculator.py
"""
Calculatrice scientifique - Application exemple pour pipeline CI/CD
Auteur : Recherche DevOps
Version : 1.0.0
"""

import math


class ScientificCalculator:
    """
    Calculatrice avec historique des opérations.
    Simule un module de recherche avec état interne.
    """

    def __init__(self):
        self.history = []  # Enregistre toutes les opérations

    def _record(self, operation: str, result: float) -> float:
        """Enregistre une opération dans l'historique."""
        self.history.append({"op": operation, "result": result})
        return result

    def add(self, a: float, b: float) -> float:
        return self._record(f"{a} + {b}", a + b)

    def subtract(self, a: float, b: float) -> float:
        return self._record(f"{a} - {b}", a - b)

    def multiply(self, a: float, b: float) -> float:
        return self._record(f"{a} * {b}", a * b)

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division par zéro interdite")
        return self._record(f"{a} / {b}", a / b)

    def square_root(self, a: float) -> float:
        if a < 0:
            raise ValueError("Racine carrée d'un nombre négatif interdite")
        return self._record(f"sqrt({a})", math.sqrt(a))

    def power(self, base: float, exp: float) -> float:
        return self._record(f"{base}^{exp}", math.pow(base, exp))

    def get_history(self) -> list:
        return self.history.copy()

    def clear_history(self):
        self.history.clear()