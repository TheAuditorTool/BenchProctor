# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest56135():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    with open('/var/app/data/' + str(json_value), 'r') as fh:
        content = fh.read()
    return content
