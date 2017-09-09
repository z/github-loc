import json
import time


def test_date_parse():
    with open("tests/data/periods.json") as f:
        unique_periods = list(set(json.loads(f.read())))
        unique_periods.sort()
    time_start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unique_periods[0]))
    time_end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unique_periods[-1]))
    assert time_start == "2009-01-24 19:00:00"
    assert time_end == "2017-09-02 20:00:00"
