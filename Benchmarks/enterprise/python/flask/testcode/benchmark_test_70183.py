# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import urllib.request


def BenchmarkTest70183():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
