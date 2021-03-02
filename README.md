# Autokeyboard:
Small python script to automate your keyboard with hotkeys.


### Setup:
Assuming you are sitting on python>=3.8
```shell
pip install -r requirements.txt
python main.py
```

### Keyboard configuration:
A json file [(config.json)](https://github.com/vokuder/Autokeyboard/blob/main/config.json) is used to configure keys.
<br>Use the following template to configure your own keys:
```shell
{
  "hotkeys": [
    {
       "trigger": "a",
       "automated_keys": ["b", "c"],
       "delay_between": 2,
       "repetitions": 2 
    }
  ]
}
```
This project highly depends on [python keyboard](https://github.com/boppreh/keyboard).
<br>So you may want to check it out before you configure your keys.
