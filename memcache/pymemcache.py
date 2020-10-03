from pymemcache.client.base import Client
client = Client(('localhost', 11211))
client.get("user")

import pickle
pickle.loads(client.get("complex"))

client.stats()['curr_items']

import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(client.stats("cachedump","1","0"))

def retrieve(key):
  result = client.get_multi(['%s-%s' % (key, i) for i in xrange(12)])
  serialized = ''
  for i in range(12):
    serialized=serialized+result[key+'-'+str(i)]
    return serialize

