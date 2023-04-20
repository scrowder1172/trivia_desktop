import requests


api_parameters = {
    "amount": 10,
    "type": "boolean"
}

opentdb_url = "https://opentdb.com/api.php"
response = requests.get(url=opentdb_url, params=api_parameters)

# raise error if return code is not 200
response.raise_for_status()

data = response.json()
question_data = data['results']

