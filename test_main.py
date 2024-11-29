import pytest
from typer.testing import CliRunner
from main import app

runner = CliRunner()


@pytest.mark.parametrize("n", [1, 2])
def test_parser(n: int):
    result = runner.invoke(app, ["parse", f"tests/parser/input_{n}.txt"])
    assert result.exit_code == 0
    assert result.stdout == ""


def test_parser_errors():
    result = runner.invoke(app, ["parse", "tests/parser/invalid_input_1.txt"])
    assert result.exit_code == 0
    assert "line 1" in result.stdout
    assert "line 3" in result.stdout
    assert "line 7" in result.stdout
    assert "line 10" in result.stdout
    assert "line 12" in result.stdout
    assert result.stdout.count("line") == 5


@pytest.mark.parametrize("n", [1, 2, 3])
def test_ast(n: int):
    result = runner.invoke(app, ["ast", f"tests/ast/input_{n}.txt"])
    assert result.exit_code == 0
    with open(f"tests/ast/output_{n}.txt", encoding="utf-8") as f:
        output = f.read()
    assert result.stdout == output


def test_sem_error_break():
    result = runner.invoke(app, ["sem", "tests/semantic/input_break.txt"])
    assert result.exit_code == 0
    assert "line 1" in result.stdout
    assert "break" in result.stdout.lower()
    assert result.stdout.count("line") == 1


def test_sem_error_continue():
    result = runner.invoke(app, ["sem", "tests/semantic/input_continue.txt"])
    assert result.exit_code == 0
    assert "line 1" in result.stdout
    assert "continue" in result.stdout.lower()
    assert result.stdout.count("line") == 1


def test_sem_error_vector():
    result = runner.invoke(app, ["sem", "tests/semantic/input_vector.txt"])
    assert result.exit_code == 0
    assert "line 1" in result.stdout
    assert "line 3" in result.stdout
    assert "line 7" in result.stdout
    assert result.stdout.count("line") == 3
    assert result.stdout.lower().count("vector") == 3


def test_sem_error_variables():
    result = runner.invoke(app, ["sem", "tests/semantic/input_variables.txt"])
    assert result.exit_code == 0
    assert "line 5" in result.stdout
    assert "line 7" in result.stdout
    assert result.stdout.count("line") == 2
    assert result.stdout.lower().count("variable") == 2


def test_sem_error_transpose():
    result = runner.invoke(app, ["sem", "tests/semantic/input_transpose.txt"])
    assert result.exit_code == 0
    assert "line 7" in result.stdout
    assert "transpose" in result.stdout.lower()
    assert result.stdout.count("line") == 1


@pytest.mark.parametrize(
    "name,line_numbers",
    [
        ("special_matrix", [1, 11]),
        ("indexing", [5, 6, 7]),
        ("indexing_bounds", [4, 11, 12]),
        ("binary_operations", [7, 8, 14, 16, 17]),
        ("comparisons", [7, 9]),
        ("compound_assignments", [10, 11, 12]),
    ],
)
def test_sem_errors(name: str, line_numbers: list):
    result = runner.invoke(app, ["sem", f"tests/semantic/input_{name}.txt"])
    assert result.exit_code == 0
    for ln in line_numbers:
        assert f"line {ln}" in result.stdout
    assert result.stdout.lower().count("line") == len(line_numbers)
