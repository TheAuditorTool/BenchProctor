# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import requests


def relay_value(value):
    return value

def BenchmarkTest61822():
    cookie_value = request.cookies.get('session_token', '')
    data = relay_value(cookie_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
