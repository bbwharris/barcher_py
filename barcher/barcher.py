import urllib
import json

class Barcher(object):
    """
    A simple client library for the Clash of Clans API in python
    """
    def __init__(self, token):
        import requests
        self.requests = requests
        self.token = token
        self.api_endpoint = "https://api.clashofclans.com/v1"
        self.timeout = 30

    """
    Generic get method to the API
    """
    def get(self, uri, params=None):
        headers = {
            'Accept': "application/json",
            'authorization': "Bearer " + self.token
        }

        url = self.api_endpoint + uri
        
        if params:
            params = json.dumps(params)

        try:
            response = self.requests.get(url, data=params, headers=headers, timeout=30)
            return response.json()
        except:
            if 400 <= response.status_code <= 599:
                return "Error " + response.status_code
    """
    Search for clans with specific criteria
    params: {
      "name": 'SomeClanName',
      "warFrequency": ['always', 'moreThanOncePerWeek','oncePerWeek','lessThenOncePerWeek','never','Unknown'],
      "locationId": 1,
      "minMembers": 20,
      "minClanPoints": 1200,
      "minClanLevel": 1-10,
      "limit": 5,
      "after": 2,
      "before": 100
    }
    """
    def search_clans(self,params):
        return self.get('/clans', params)

    """
    Find a specific clan by clan tag (omit # symbol)
    ex: #123456 would be
    client.find_clan("123456")
    """
    def find_clan(self, tag):
        return self.get('/clans/%23' + tag)

    """
    Retrieve member for a specific clan tag
    client.clan_members_for("123456")
    """
    def clan_members_for(self, tag)
        return self.get('/clans/%23' + tag + '/members')
    """
    return all locations for clash players
    client.locations()
    """
    def locations(self):
        return self.get('/locations')

    """
    return specific location by its id
    client.location(4)
    """
    def location(self,id):
        return self.get('/locations/' + id)

    """
    return all rankings associated with a given location:
    client.rankings_at_location(1, 5)
    """
    def rankings_at_location(self, location_id, ranking_id):
        return self.get('/locations/' + location_id + '/rankings/' + ranking_id)
    
    """
    return all leagues
    client.leagues()
    """
    def leagues(self):
        return self.get('/leagues')