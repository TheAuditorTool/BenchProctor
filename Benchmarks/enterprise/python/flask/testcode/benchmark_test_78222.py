# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest78222():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = ' '.join(str(json_value).split())
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
