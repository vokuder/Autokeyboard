import os
import time
import json
import threading
import keyboard


def execute_hotkey(hotkey_config):
    print(f'Press "{hotkey_config["trigger"]}" to execute: {hotkey_config["keys"]} with {hotkey_config["delay"]} seconds delay and {hotkey_config["repetitions"]} repetitions')
    while True:
        keyboard.wait(hotkey_config["trigger"])
        for i in range(hotkey_config["repetitions"]):
            for key in hotkey_config["keys"]:
                keyboard.press_and_release(key)
                time.sleep(hotkey_config["delay"])


def get_config():
    with open(os.path.join(os.getcwd(), "config.json"), "r") as config_file:
        return json.load(config_file)


if __name__ == '__main__':
    for hotkey in get_config()["hotkeys"]:
        threading.Thread(target=execute_hotkey, args=(hotkey,), daemon=True).run()
