import os
import json
import base64
import argparse
import urllib.request
import urllib.error
import locale
import time
from .config import conf
from .__about__ import __version__

locale.setlocale(locale.LC_ALL, '')


def main():

    args = parse_args()

    user = args.user
    token = conf['token']

    repos_json = get_user_repos(user, token)

    if len(repos_json) == 0:
        print('Unable to find any repos, visit https://github.com/{} or try again'.format(user))
        raise SystemExit

    user_repos = []
    for repo in repos_json:
        if not repo['fork']:
            user_repos.append(repo['full_name'])

    lines_total = 0
    periods = []
    for repo in user_repos:
        code_freq = get_repo_stats(repo, token)
        for period in code_freq:
            periods.append(period[0])
            lines_total += int(period[1]) + int(period[2])

    unique_periods = list(set(periods))
    unique_periods.sort()

    time_start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unique_periods[0]))
    time_end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unique_periods[-1]))

    lines_total_pretty = locale.format("%d", lines_total, grouping=True)

    print(user + ' has written ' + lines_total_pretty + ' lines of code between all repositories they own from ' + time_start + ' to ' + time_end)


def get_repo_stats(repo, token):

    repo_stats_url = 'https://api.github.com/repos/' + repo + '/stats/code_frequency'
    user = repo.split('/')[0]
    data = aqi_request(repo_stats_url, user, token)
    repo_stats_json = json.loads(data.decode("utf-8"))

    return repo_stats_json


def get_user_repos(user, token):

    user_url = 'https://api.github.com/users/' + user + '/repos'
    data = aqi_request(user_url, user, token)
    repos_json = json.loads(data.decode("utf-8"))

    return repos_json


def aqi_request(url, user, token):

    req = urllib.request.Request(url)

    if token:
        auth = base64.b64encode(bytes(user, encoding='utf-8') + b':' + bytes(token, encoding='utf-8'))
        req.add_header("Authorization", b'Basic ' + auth)
    try:
        response = urllib.request.urlopen(req)
        data = response.read()
    except urllib.error.HTTPError as err:
        print("API Request Error: {0}".format(err))
        print("Please add your token to ~/.githubloc.ini")
        raise SystemExit

    return data


def parse_args():

    parser = argparse.ArgumentParser(
            description='Count how many lines of code have been commited by a github user')

    parser.add_argument('--version', action='version',
                        version='%(prog)s {version}'.format(version=__version__))

    parser.add_argument('--user', '-u', nargs='?', type=str,
                        help='github username', required=True)
    parser.add_argument('--token', '-t', nargs='?', type=str,
                        help='github personal access token (overrides the one in config.ini)')

    return parser.parse_args()


if __name__ == "__main__":
    main()
