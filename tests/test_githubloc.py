import json
import time


def test_date_parse():
    with open("tests/data/periods.json") as f:
        unique_periods = list(set(json.loads(f.read())))
    time_start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unique_periods[0]))
    time_end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unique_periods[-1]))
    assert time_start == "2013-10-05 20:00:00"
    assert time_end == "2014-09-27 20:00:00"
