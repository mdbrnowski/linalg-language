from typer.testing import CliRunner
from main import app

runner = CliRunner()


def test_ast():
    result = runner.invoke(app, ["ast", "tests/ast/input_1.txt"])
    assert result.exit_code == 0
    with open("tests/ast/output_1.txt", encoding="utf-8") as f:
        output = f.read()
    assert result.stdout == output
