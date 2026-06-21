# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request
import json


def BenchmarkTest39836():
    host_value = request.headers.get('Host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
