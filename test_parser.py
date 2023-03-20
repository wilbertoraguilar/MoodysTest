import typer
from typer.testing import CliRunner
from parsefile import main

app = typer.Typer()
app.command()(main)
runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["input.dat"])
    assert result.exit_code == 0
    assert "1 3 N" in result.output
    assert "5 1 E" in result.output
