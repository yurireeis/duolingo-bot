"""Unofficial API for duolingo.com"""
import requests

__version__ = "0.1"
__author__ = "Yuri Reis"
__email__ = "yuri.reis@msn.com"
__url__ = "https://github.com/yurireeis/duolingo-bot"


class SocialBase(object):
    def __init__(self, username, password, network='qa', api='p', app='p'):
        self.username = username
        self.password = password
        self.api = 'https://{}-api.socialbase.com.br/v3'.format(api)
        self.app = 'https://{}-app.socialbase.com.br'.format(app)
        self.url = 'https://{}.socialbase.com.br'.format(network)
        self.session = requests.Session()
        self.headers = {
            'app': {
                'accept': "application/json",
                'content-type': "application/json",
                'origin': self.url,
                'referer': self.url,
            },
            'api': {
                'content-type': "application/json",
                'accept': "application/json",
            },
        }
        self._login()

        if not self.username and not self.password:
            raise Exception('Needs username or password information')

    def _make_req(self, url, data=None, api=None):
        """

        :param url:
        :param data:
        :param api:
        :return:
        """
        if not api:
            raise Exception('You need to pass the api that you want to use')

        req = None
        if data:
            req = requests.Request('POST', url, headers=self.headers[api], json=data, cookies=self.session.cookies)

        if not req:
            raise Exception('Request failed')

        prepped = req.prepare()
        return self.session.send(prepped)

    def _login(self):
        """
        Authenticate through SocialBase desired network
        ex.: ``'https://p-app.socialbase.com.br/authentication'``.
        """
        url = self.app + '/authentication'
        data = {'username': self.username, 'password': self.password, 'type': 'credentials'}
        attempt = self._make_req(url, data, 'app').json()

        if attempt.get('access_token'):
            self.headers['api']['authorization'] = 'Bearer {}'.format(attempt.get('access_token'))
        else:
            raise Exception("Login failed")

    def post(self, text=None, group_id=None):
        """
        Post in SocialBase Network user's activity
        ``'https://p-api.socialbase.com.br/v3/activities``
        if you set a group id, your post will be done in the desired group
        """
        url = self.api + '/activities'
        if not text:
            raise Exception('You must pass a text to post')

        data = {"body": text}

        if group_id:
            data['target'] = {'id': group_id, 'type': 'group'}

        attempt = self._make_req(url, data, 'api').json()

        if attempt.get('actionId'):
            return True

        raise Exception('Post failed')
