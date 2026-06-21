# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest76845():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
