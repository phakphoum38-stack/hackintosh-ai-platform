import json

def load_dataset():

    with open("database/boot_dataset.json") as f:
        return json.load(f)
