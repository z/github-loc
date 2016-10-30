import os
import githubloc.util as util

config_file = '.githubloc.ini'
home = os.path.expanduser('~')
config_file_with_path = os.path.join(home, config_file)

util.check_if_not_create(config_file_with_path, 'config/githubloc.ini')

config = util.parse_config(config_file_with_path)

conf = {
    'token': os.path.expanduser(config['token']),
}
