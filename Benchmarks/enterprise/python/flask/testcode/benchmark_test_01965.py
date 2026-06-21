# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request
import json


def BenchmarkTest01965():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
