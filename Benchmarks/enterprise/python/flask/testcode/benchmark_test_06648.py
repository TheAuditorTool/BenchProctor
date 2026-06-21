# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest06648():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
