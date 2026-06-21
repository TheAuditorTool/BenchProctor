# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import request, jsonify
import urllib.request


def BenchmarkTest25753():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
