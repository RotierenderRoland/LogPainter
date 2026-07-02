# LogPainter

LogPainter is a small Python CLI tool that colorizes log files based on configurable YAML rules.  
It allows you to define patterns and assign ANSI colors to matching log lines.

## Features

- Pattern-based log highlighting
- YAML configuration
- ANSI color output
- Log streaming
- Unit tests with pytest
- Linting with flake8
- GitHub Actions CI integration
- Installable as a Python package

---

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd LogPainter
```

Install the package in editable mode:

```bash
pip install -e .
```

For development (including pytest):

```bash
pip install -e ".[dev]"
```

---

## Usage

Run the CLI tool:

```bash
cat test.log | logpainter --config example-config.yamlg
```

If not installed as a CLI entry point:

```bash
cat test.log | python -m logpainter.logpainter --config example-config.yaml
```

---

## Configuration

Example `example-config.yaml`:

```yaml
rules:
  - pattern: ERROR
    color: red
  - pattern: WARNING
    color: yellow
  - pattern: INFO
    color: green
```

Supported colors:

- red
- yellow
- green
- blue
- cyan

---

## Project Structure

```
LogPainter/
├── logpainter/
│   ├── __init__.py
│   ├── colors.py
│   ├── logpainter.py
│   └── tests/
├── example-config.yaml
├── pyproject.toml
├── README.md
└── test.log
```

---

## Development

Run tests:

```bash
pytest -q
```

Run linting:

```bash
flake8 .
```

---

## CI

The project includes a GitHub Actions workflow that:

- Installs dependencies
- Runs flake8
- Executes pytest

---

## Requirements

- Python 3.9+
- PyYAML

---

## Future Improvements

- Regex support
- Case-insensitive matching
- Rule priority handling

---

## License

MIT License 