#!/usr/bin/env python3
import yaml
import os
import argparse
from colors import color_map


def load_config(config_path):
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


def extract_lines(log_file: str) -> list[str]:
    file_content = []
    with open(log_file, 'r') as file:
        for line in file:
            file_content.append(line)
    return file_content


def colorise_line(line: str, config: dict) -> str:
    for rule in config['rules']:
        if rule['pattern'] in line:
            return color_map[rule['color']](line.strip())
    return line.strip()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Colorize log files based on patterns in configuration")
    parser.add_argument("--config", required=True,
                        help="Path to YAML configuration file")
    parser.add_argument("--logfile", required=True,
                        help="Path to the log file")
    args = parser.parse_args()

    config = load_config(args.config)
    log_file_content = extract_lines(args.logfile)
    for line in log_file_content:
        print(colorise_line(line, config))
