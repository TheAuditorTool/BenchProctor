# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import urllib.request


def BenchmarkTest13806():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', json_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = json_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
