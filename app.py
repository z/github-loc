import urllib.request
import json
import argparse


def main():
    args = parse_args()

    user = args.user

    repos_json = get_user_repos(user)

    user_repos = []
    for repo in repos_json:
        if not repo['fork']:
            user_repos.append(repo['full_name'])

    lines_total = 0
    for repo in user_repos:
        code_freq = get_repo_stats(repo)
        for period in code_freq:
            lines_total += int(period[1]) + int(period[2])

    print(user + ' has written ' + str(lines_total) + ' lines of code over all repositories they own')


def get_repo_stats(repo):
    repo_stats_url = 'https://api.github.com/repos/' + repo + '/stats/code_frequency'

    req = urllib.request.Request(repo_stats_url)
    response = urllib.request.urlopen(req)
    data = response.read()

    repo_stats_json = json.loads(data.decode("utf-8"))

    return repo_stats_json


def get_user_repos(user):
    user_url = 'https://api.github.com/users/' + user + '/repos'

    req = urllib.request.Request(user_url)
    response = urllib.request.urlopen(req)
    data = response.read()

    repos_json = json.loads(data.decode("utf-8"))

    return repos_json


def parse_args():

    parser = argparse.ArgumentParser(description='Figure out how many lines of code have been added by a github user')

    parser.add_argument('--user', '-u', nargs='?', type=str, help='github username', required=True)

    return parser.parse_args()


if __name__ == "__main__":
    main()
