# tests/test_calculator.py
"""
Suite de tests unitaires pour ScientificCalculator.
Chaque test = un contrat que notre code doit respecter.
"""

import sys
import os
import pytest

# Permet d'importer depuis src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import ScientificCalculator


# ─── FIXTURES ────────────────────────────────────────────────────────────────

@pytest.fixture
def calc():
    """Fournit une instance fraîche pour chaque test."""
    return ScientificCalculator()


# ─── TESTS DES OPÉRATIONS DE BASE ────────────────────────────────────────────

class TestBasicOperations:

    def test_addition(self, calc):
        assert calc.add(2, 3) == 5

    def test_addition_negative(self, calc):
        assert calc.add(-1, -1) == -2

    def test_subtraction(self, calc):
        assert calc.subtract(10, 4) == 6

    def test_multiply(self, calc):
        assert calc.multiply(3, 7) == 21

    def test_divide(self, calc):
        assert calc.divide(10, 2) == 5.0

    def test_divide_by_zero_raises(self, calc):
        with pytest.raises(ValueError, match="Division par zéro"):
            calc.divide(5, 0)


# ─── TESTS DES OPÉRATIONS SCIENTIFIQUES ──────────────────────────────────────

class TestScientificOperations:

    def test_square_root(self, calc):
        assert calc.square_root(9) == 3.0

    def test_square_root_negative_raises(self, calc):
        with pytest.raises(ValueError, match="négatif"):
            calc.square_root(-4)

    def test_power(self, calc):
        assert calc.power(2, 10) == 1024.0


# ─── TESTS DE L'HISTORIQUE ────────────────────────────────────────────────────

class TestHistory:

    def test_history_records_operations(self, calc):
        calc.add(1, 2)
        calc.multiply(3, 4)
        history = calc.get_history()
        assert len(history) == 2

    def test_history_clear(self, calc):
        calc.add(1, 1)
        calc.clear_history()
        assert len(calc.get_history()) == 0

    def test_history_is_copy(self, calc):
        """Vérifie que get_history() retourne une copie, pas une référence."""
        calc.add(5, 5)
        h = calc.get_history()
        h.append({"op": "fake", "result": 999})
        assert len(calc.get_history()) == 1  # L'original ne doit pas changer
