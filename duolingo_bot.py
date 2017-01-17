from datetime import datetime
import os
from duolingo import Duolingo
from socialbase import SocialBase
from support import get_list_formmated

SB_USERNAME = os.getenv('SB_USERNAME')
PASSWORD = os.getenv('PASSWORD')
DUO_USERNAME = os.getenv('DUO_USERNAME')
NETWORK = os.getenv('NETWORK_NAME')
APP = os.getenv('APP')
API = os.getenv('API')

today = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
leaderboard = {}
lingo = Duolingo(DUO_USERNAME, PASSWORD)
base = SocialBase(SB_USERNAME, PASSWORD, NETWORK, APP, API)
leaderboard['week'] = lingo.get_leaderboard('week', today)
leaderboard['month'] = lingo.get_leaderboard('month', today)
post = get_list_formmated(leaderboard['week'])
base.post(post, group_id=923)
