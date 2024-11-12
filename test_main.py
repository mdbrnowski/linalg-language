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


def test_ast():
    result = runner.invoke(app, ["ast", "tests/ast/input_1.txt"])
    assert result.exit_code == 0
    with open("tests/ast/output_1.txt", encoding="utf-8") as f:
        output = f.read()
    assert result.stdout == output
