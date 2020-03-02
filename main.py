""" github practive activity script """

# imports
import sys
import datetime as dt
import requests
# ==================================

# Use Like python githubber.py JASchilz
# (or another user name)

# -----------------------------------
if __name__ == "__main__":
    USERNAME = sys.argv[1]

    # 1. Retrieve a list of "events" associated with the given user name
    RESPONSE = requests.get('https://api.github.com/users/{}/events'.format(USERNAME))
    EVENTS = [(RESPONSE.json()[ix]['type'][0:-5],
               RESPONSE.json()[ix]['created_at'])
              for ix in range(len(RESPONSE.json()))]

    # 2. Print out the time stamp associated with the first event in that list.
    FIRST_DATE = dt.datetime.strptime(EVENTS[0][1], "%Y-%m-%dT%H:%M:%SZ")
    print(dt.datetime.strftime(FIRST_DATE, "%Y-%m-%d %H:%M:%S"))
