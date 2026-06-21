# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest18920():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = ' '.join(str(json_value).split())
    return str(data), 200, {'Content-Type': 'text/html'}
