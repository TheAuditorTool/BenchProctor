# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest08927():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
