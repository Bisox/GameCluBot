import json

# dict_token_api = '{"data":{"token": "6442729239:AAHHVar6z-_ZZsxbgOAFzztKzOSqag3Amuc", "api": "7d173332332ff816eb05842cec22f61b"}}'


# with open("token_api.json", 'w') as write_file:
#     json.dump(dict_token_api, write_file)





with open("token_api.json", 'r') as f:
    data = json.load(f)
a = json.loads(data)



