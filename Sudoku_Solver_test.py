import pytest
from Sudoku_Solver import *


def test_length_units():
    assert len(units) == 81
    for square in units:
        assert len(units[square]) == 3


def test_length_peers():
    assert len(peers) == 81
    for square in peers:
        assert len(peers[square]) == 20


def test_parse_grid_invalid_input_length_raises_valueerror():
    with pytest.raises(ValueError):
        parse_grid("001527")


def test_parse_grid_invalid_characters_raises_valueerror():
    with pytest.raises(ValueError):
        parse_grid("A" * 81)


def test_parse_grid_valid_input_returns_grid_as_dictionary():
    result = parse_grid("003020600900305001001806400008102900700000008006708200002609500800203009005010300")
    assert len(result) == 81
    assert result["A1"] == "4"
    assert result["I9"] == "2"
