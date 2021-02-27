import os
import json
import threading
import keyboard


WORKING_DIR = os.getcwd()
KEY_CONFIG_FILE = os.path.join(WORKING_DIR, "keys.json")


def get_key_config(config_file):
    print("Loading key config ...")
    with open(config_file, "r") as key_config:
        return json.load(key_config)


def trigger_key_pressed():
    pass
