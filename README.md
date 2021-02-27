# Autokeyboard:
Small python script to automate keyboard events.


### Setup:
Assuming you are sitting on python>=3.7
```shell
pip install -r requirements.txt
python main.py
```

### Keyboard configuration:
A json file (config.json) is used to configure keys.
<br>Use the following template to configure your own keys:
```shell
{
  "keys": [
    {
       "trigger": "a",
       "automated_keys": ["b", "c"],
       "delay_between": 2,
       "repetitions": 2 
    }
  ]
}
```
