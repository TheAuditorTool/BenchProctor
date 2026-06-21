# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest05270():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = str(json_value).replace('\x00', '')
    return str(data), 200, {'Content-Type': 'text/html'}
