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


def print_colored_logs(log_file, config):
    with open(log_file, 'r') as file:
        for line in file:
            colored = False
            for rule in config['rules']:
                if rule['pattern'] in line:
                    print(color_map[rule['color']](line.strip()))
                    colored = True
                    break
            if not colored:
                print(line.strip())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Colorize log files based on patterns in configuration")
    parser.add_argument("--config", required=True,
                        help="Path to YAML configuration file")
    parser.add_argument("--logfile", required=True,
                        help="Path to the log file")
    args = parser.parse_args()

    config = load_config(args.config)
    print_colored_logs(args.logfile, config)
