import os
import json
import base64
import argparse
import configparser
import urllib.request
import locale
import time

locale.setlocale(locale.LC_ALL, '')


def main():

    args = parse_args()
    config = read_config('config.ini')

    user = args.user
    token = get_token(args.token, config)

    repos_json = get_user_repos(user, token)

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

    response = urllib.request.urlopen(req)
    data = response.read()

    return data


def get_token(args_token, config):

    token = False

    if args_token:
        token = args_token

    if config and 'token' in config:
        token = config['token']

    return token


def read_config(config_file):

    if not os.path.isfile(config_file):
        print('Warning:' + config_file + ' not found, processing request anonymously.')
        return False

    config = configparser.ConfigParser()
    config.read(config_file)

    return config['default']


def parse_args():

    parser = argparse.ArgumentParser(description='Count how many lines of code have been commited by a github user')

    parser.add_argument('--user', '-u', nargs='?', type=str, help='github username', required=True)
    parser.add_argument('--token', '-t', nargs='?', type=str, help='github personal access token (overrides the one in config.ini)')

    return parser.parse_args()


if __name__ == "__main__":
    main()
