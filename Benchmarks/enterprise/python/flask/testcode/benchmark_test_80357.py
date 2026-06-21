# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest80357():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    prefix = ''
    data = prefix + str(json_value)
    return str(data), 200, {'Content-Type': 'text/html'}
