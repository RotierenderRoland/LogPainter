import pytest
from logpainter.logpainter import load_config, extract_lines, colorise_line
from logpainter import colors


def test_load_config_file_not_found(tmp_path):
    missing = tmp_path / "missing.yml"
    with pytest.raises(FileNotFoundError):
        load_config(str(missing))


def test_load_config_invalid_yaml(tmp_path):
    cfg = tmp_path / "config.yml"
    cfg.write_text("rules:\n  - pattern: [unclosed\n", encoding="utf-8")

    with pytest.raises(ValueError):
        load_config(str(cfg))


def test_load_config_valid_yaml(tmp_path):
    cfg = tmp_path / "config.yml"
    cfg.write_text(
        "rules:\n"
        "  - pattern: ERROR\n"
        "    color: red\n"
        "  - pattern: WARNING\n"
        "    color: yellow\n",
        encoding="utf-8",
    )

    config = load_config(str(cfg))
    assert isinstance(config, dict)
    assert "rules" in config
    assert isinstance(config["rules"], list)
    assert config["rules"][0]["pattern"] == "ERROR"
    assert config["rules"][0]["color"] == "red"


def test_extract_lines_keeps_newlines(tmp_path):
    logfile = tmp_path / "app.log"
    logfile.write_text("a\nb\nc\n", encoding="utf-8")

    lines = extract_lines(str(logfile))
    assert lines == ["a\n", "b\n", "c\n"]


def test_colorise_line_matches_and_colors():
    config = {"rules": [{"pattern": "ERROR", "color": "red"}]}
    out = colorise_line("ERROR boom\n", config)
    assert out == colors.red("ERROR boom")


def test_colorise_line_no_match_returns_stripped_line():
    config = {"rules": [{"pattern": "ERROR", "color": "red"}]}
    out = colorise_line("INFO ok\n", config)
    assert out == "INFO ok"


def test_colorise_line_first_match_wins():
    config = {
        "rules": [
            {"pattern": "ERR", "color": "yellow"},
            {"pattern": "ERROR", "color": "red"},
        ]
    }
    out = colorise_line("ERROR boom\n", config)
    assert out == colors.yellow("ERROR boom")


def test_colorise_line_unknown_color_raises_keyerror():
    config = {"rules": [{"pattern": "ERROR", "color": "magenta"}]}
    with pytest.raises(KeyError):
        colorise_line("ERROR boom\n", config)
