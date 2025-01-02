#!/usr/bin/env python3
import yaml
import os
import argparse
from colorama import Fore, Style, init

init()

def load_config(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"The configuration file '{config_path}' does not exist.")
    with open(config_path,"r") as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as YAMLError:
            raise ValueError(f"Error parsing YAML file: {e}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {e}")

def prin_colored_logs():
    color_map = {
        "red": Fore.RED,
        "yellow": Fore.YELLOW,
        "green": Fore.GREEN,
        "white": Fore.WHITE,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
    }