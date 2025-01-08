import json

def get_younger_futhark_json():
    # Read in the yournger futhark json file
    with open('younger_futhark.json') as f:
        data = json.load(f)
    return data

def get_elder_futhark_json():
    # Read in the elder futhark json file
    with open('elder_futhark.json') as f:
        data = json.load(f)
    return data


