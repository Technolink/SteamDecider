from __future__ import print_function
import json

print('Loading function')


def find_games(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print("Context: " + json.dumps(context, indent=2))
    
    return context;
