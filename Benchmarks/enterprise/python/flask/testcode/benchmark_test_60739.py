# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest60739():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    return '<!-- diagnostic build token: ' + str(json_value) + ' -->', 200, {'Content-Type': 'text/html'}
