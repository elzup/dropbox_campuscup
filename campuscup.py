import commands
import gzip
import re
import code
import json
from bs4 import BeautifulSoup

query = "{your session}"
commands.getoutput(query)
f = gzip.open('tmp.gz', 'rb')
html = ''.join(f.readlines())
f.close()


regex = 'StudentPromoDashboardController, ({.*}), null'
m = re.search(regex, html)
print(m.group(1))
con = json.loads(m.group(1))
# {"school": {"num-students": 83, "space-earned": 0, "name": "Tokyo Denki University", "points-earned": 2254, "tiers": [{"points-needed": -1342, "complete": true, "space": 3}, {"points-needed": 483, "complete": false, "space": 8}, {"points-needed": 3221, "complete": false, "space": 15}, {"points-needed": 12347, "complete": false, "space": 25}]}, "links": {"dropbox_terms": "/privacy#terms", "help": "/help/9131", "student_promo_terms": "https://dropboxstatic.com/static/docs/campuscup/2015_campus_cup_terms_of_service.pdf"}, "actions": {"has_created_shared_folder": {"started": true, "completed": true}, "has_created_file_request": {"started": true, "completed": true}, "has_created_shared_link": {"started": false, "completed": false}, "has_linked_mobile_client": {"started": true, "completed": true}, "has_linked_desktop_client": {"started": true, "completed": true}, "num_referred_friends": {"started": false, "completed": false}}, "expFeaturesOnTop": false, "numSuccessfulReferrals": 0, "expShowLeaderboard": false, "jsComponentId": "component11660", "triplePointsEndDate": 1443499530, "pointsEarned": 40}
point = con['school']['points-earned']
print(point)
