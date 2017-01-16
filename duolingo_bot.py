#!/home/yurireis/env/duolingo/bin python3
from datetime import datetime

import os

from duolingo import Duolingo
from socialbase import SocialBase
from support import get_list_formmated

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD_NAME')
NETWORK = os.getenv('NETWORK_NAME')
APP = os.getenv('APP')
API = os.getenv('API')

today = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
leaderboard = {}
lingo = Duolingo('sb_challenge', 'socialbase')
base = SocialBase(USERNAME, PASSWORD, NETWORK, APP, API)
leaderboard['week'] = lingo.get_leaderboard('week', today)
leaderboard['month'] = lingo.get_leaderboard('month', today)
post = get_list_formmated(leaderboard['week'])
base.post(post, group_id=923)
