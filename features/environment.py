import json

def before_all(context):
    with open('config.json') as config_file:
        config = json.load(config_file)
    context.API_BASE_URL = config['API_BASE_URL']