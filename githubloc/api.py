import json
import base64
import urllib
import urllib.request
import urllib.error


class Api:

    def __init__(self, user, token):
        self.user = user
        self.token = token

    def aqi_request(self, url, retry=True):

        req = urllib.request.Request(url)

        if self.token:
            auth = base64.b64encode(bytes(self.user, encoding='utf-8') +
                                    b':' + bytes(self.token, encoding='utf-8'))
            req.add_header("Authorization", b'Basic ' + auth)

        try:
            response = urllib.request.urlopen(req)
            if response.status != 200 and retry:
                self.aqi_request(url, retry=False)
        except urllib.error.HTTPError as err:
            print("API Request Error: {0}".format(err))
            print("Please add your token to ~/.githubloc.ini if you haven't already")
            raise UserWarning

        return response

    def get_repo_stats(self, repo):

        url = "https://api.github.com/repos/{}/stats/code_frequency".format(repo)
        response = self.aqi_request(url)
        data = {}
        if response.status == 200:
            data = json.loads(response.read().decode("utf-8"))

        return data

    def get_user_repos(self):

        url = 'https://api.github.com/users/{}/repos'.format(self.user)
        try:
            response = self.aqi_request(url)
        except UserWarning:
            print('Ut oh! Does that user really exist on github?')
            raise SystemExit
        data = {}
        if response.status == 200:
            data = json.loads(response.read().decode("utf-8"))

        return data
