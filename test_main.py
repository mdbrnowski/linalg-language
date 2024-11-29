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


@pytest.mark.parametrize(
    "name,line_numbers,additional",
    [
        ("break", [1], "break"),
        ("continue", [1], "continue"),
        ("vector", [1, 3, 7], "vector"),
        ("variables", [5, 7], "variable"),
        ("transpose", [7], "transpose"),
        ("special_matrix", [1, 11], "matrix"),
        ("indexing", [5, 6, 7], ""),
        ("indexing_bounds", [4, 11, 12], "out of bounds"),
        ("binary_operations", [7, 8, 14, 16, 17], "binary operation"),
        ("comparisons", [7, 9], "comparison"),
        ("compound_assignments", [10, 11, 12], "assignment"),
        ("ranges", [9], "range"),
    ],
)
def test_sem_errors(name: str, line_numbers: list[int], additional: str):
    result = runner.invoke(app, ["sem", f"tests/semantic/input_{name}.txt"])
    assert result.exit_code == 0
    for ln in line_numbers:
        assert f"line {ln}" in result.stdout
    assert result.stdout.lower().count("line") == len(line_numbers)
    if additional:
        assert result.stdout.lower().count(additional) == len(line_numbers)
