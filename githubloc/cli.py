import argparse
import locale
import time
from githubloc import api
from githubloc.config import conf
from githubloc.__about__ import __version__

locale.setlocale(locale.LC_ALL, '')


def main():

    args = parse_args()

    user = args.user
    token = conf['token']

    session = api.Api(user, token)

    repos_json = session.get_user_repos()

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
        code_freq = session.get_repo_stats(repo)
        for period in code_freq:
            periods.append(period[0])
            lines_total += int(period[1]) + int(period[2])

    unique_periods = list(set(periods))
    unique_periods.sort()

    if len(unique_periods) > 1:
        time_start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unique_periods[0]))
        time_end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unique_periods[-1]))

        lines_total_pretty = locale.format("%d", lines_total, grouping=True)

        print('{} has written {} lines of code between all repositories they own from {} to {}'.format(user, lines_total_pretty, time_start, time_end))
    else:
        print('hmmm, I had trouble getting the data, try one more time')


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
