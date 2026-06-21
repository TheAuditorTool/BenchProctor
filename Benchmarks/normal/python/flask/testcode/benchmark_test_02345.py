# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest02345():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    link_path = os.path.join('/var/app/data', str(json_value))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
