#!/usr/bin/env python3
import yaml
import os
import sys
import argparse
from .colors import color_map
import re


def load_config(config_path: str) -> dict:
    if not os.path.exists(config_path):
        raise FileNotFoundError(
            f"The configuration file '{config_path}' does not exist.")
    with open(config_path, "r") as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as YAMLError:
            raise ValueError(f"Error parsing YAML file: {YAMLError}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {e}")


def validate_config(config: dict) -> None:
    if config is None:
        raise ValueError('Config is empty')
    validate_rules(config)
    validate_colors(config)


def validate_colors(config: dict) -> None:
    if not all(rule.get('color') in color_map.keys() for rule in config.get('rules')):
        raise ValueError(
            f'Not all colors are valid. Valid colors are {",".join(color_map.keys())}')


def validate_rules(config: dict) -> None:
    if not all('literal' in rule or 'pattern' in rule for rule in config.get('rules')):
        raise ValueError('Every rule needs a literal or pattern')


def colorise_line(line: str, config: dict) -> str:
    for rule in config.get('rules'):
        literal = rule.get("literal")
        pattern = rule.get("pattern")
        if literal and rule.get('literal') in line:
            return color_map[rule.get('color')](line.strip())
        elif pattern and re.search(rule.get('pattern'), line):
            return color_map[rule.get('color')](line.strip())
    return line.strip()


def main():
    parser = argparse.ArgumentParser(
        description="Colorize logs from stdin based on patterns in configuration")
    parser.add_argument("--config", required=True,
                        help="Path to YAML configuration file")
    args = parser.parse_args()

    config = load_config(args.config)
    validate_config(config)

    for line in sys.stdin:
        print(colorise_line(line, config))


if __name__ == "__main__":
    main()
