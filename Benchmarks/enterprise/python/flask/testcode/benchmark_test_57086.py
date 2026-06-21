# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request
import json


def BenchmarkTest57086():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
