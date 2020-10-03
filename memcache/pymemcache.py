from pymemcache.client.base import Client
client = Client(('localhost', 11211))
client.get("user")

import pickle
pickle.loads(client.get("complex"))

client.stats()['curr_items']

import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(client.stats("cachedump","1","100"))


