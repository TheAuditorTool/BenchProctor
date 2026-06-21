# SPDX-License-Identifier: Apache-2.0
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest30393():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
