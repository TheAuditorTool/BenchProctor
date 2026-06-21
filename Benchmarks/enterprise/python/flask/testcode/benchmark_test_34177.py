# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request
import json


def BenchmarkTest34177():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
