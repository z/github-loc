import json
import base64
import urllib
import urllib.request
import urllib.error


class Api:

    def __init__(self, user, token):
        self.user = user
        self.token = token

    def aqi_request(self, url):

        req = urllib.request.Request(url)

        if self.token:
            auth = base64.b64encode(bytes(self.user, encoding='utf-8') +
                                    b':' + bytes(self.token, encoding='utf-8'))
            req.add_header("Authorization", b'Basic ' + auth)
        try:
            response = urllib.request.urlopen(req)
            data = response.read()
        except urllib.error.HTTPError as err:
            print("API Request Error: {0}".format(err))
            print("Please add your token to ~/.githubloc.ini")
            raise SystemExit

        return data

    def get_repo_stats(self, repo):

        url = "https://api.github.com/repos/{}/stats/code_frequency".format(repo)
        data = self.aqi_request(url)
        response = json.loads(data.decode("utf-8"))

        return response

    def get_user_repos(self):

        url = 'https://api.github.com/users/{}/repos'.format(self.user)
        data = self.aqi_request(url)
        response = json.loads(data.decode("utf-8"))

        return response
