import requests

def find_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    return response.json()

