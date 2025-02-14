import main
import pytest

def test_integration(capsys):
    filename = "test_input_commands.txt"
    commands = main.read_commands_from_file(filename)
    main.process_commands(commands)

    captured = capsys.readouterr().out.strip()

    with open("test_expected_output.txt", "r") as f:
        expected_output = f.read().strip()

    assert captured == expected_output, "Integration test failed: output does not match expected output"

