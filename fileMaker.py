import re
import requests
import datetime
import json
#Concurrent requests might be a good idea for this
from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession
from config import apikey


"""
	Lets make some nice json files so I can understand the data format easier
"""


files = ["tourneys", "games", "players", "regions", "elo", "characters"]


# for request in files:
# 	curRequest = requests.get("https://api.ausmash.com.au/%s" % request, headers={"X-ApiKey": apikey})
# 	jsonInfo = curRequest.json()
# 	with open("%s.json" % request, "w", encoding="utf-8") as file:
# 		json.dump(jsonInfo, file, indent=4, separators=(',',': '), sort_keys=True, ensure_ascii=False)

eloRequest = requests.get("https://api.ausmash.com.au/tourneys/10640", headers={"X-ApiKey": apikey})
jsonInfo = eloRequest.json()
with open("bam10.json", "w", encoding="utf-8") as file:
		json.dump(jsonInfo, file, indent=4, separators=(',',': '), sort_keys=True, ensure_ascii=False)
