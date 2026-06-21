# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest30442():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    return str(data), 200, {'Content-Type': 'text/html'}
