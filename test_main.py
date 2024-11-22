import pytest
from typer.testing import CliRunner
from main import app

runner = CliRunner()


def test_parser_basic():
    result = runner.invoke(app, ["parse", "tests/parser/input_1.txt"])
    assert result.exit_code == 0
    assert result.stdout == ""


def test_parser_loops():
    result = runner.invoke(app, ["parse", "tests/parser/input_2.txt"])
    assert result.exit_code == 0
    assert result.stdout == ""


def test_parser_error():
    result = runner.invoke(app, ["parse", "tests/parser/invalid_input_1.txt"])
    assert result.exit_code == 0
    assert "line 1" in result.stdout
    assert "line 3" in result.stdout
    assert "line 7" in result.stdout
    assert "line 10" in result.stdout
    assert "line 12" in result.stdout
    assert result.stdout.count("line") == 5


@pytest.mark.parametrize("n", [1, 2, 3])
def test_ast(n):
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
    assert result.stdout.count("vector") == 3
