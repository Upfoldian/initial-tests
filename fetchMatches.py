import re
import requests
import datetime
import json
#Concurrent requests might be a good idea for this
from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession
from config import apikey

"""
	I think the current optimal way to fetch all the matches initially is:
		- 1 request GET /tourneys
			- fetches all the tournament IDs on record
		- 1 x numTourneys GET /tourneys/{id}
			- need to get all the eventIDs to fetch matches
			- this could filter event by games
		- 1 x numEvents GET /events/{id}/matches
			- this returns all the matches in an event
	Request count = tournaments + numTourney + (eventsPerTourney * numTourneys)
	Currently 2048 tournaments and assume 4 events per tournament
	Current estimates 	= 1 + 2048 + 2048*4
						= 10241
	At current API ratelimits that's at least 5 minutes at 2000 requests/minute
"""