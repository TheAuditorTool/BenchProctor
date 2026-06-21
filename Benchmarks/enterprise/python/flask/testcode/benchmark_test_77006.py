# SPDX-License-Identifier: Apache-2.0
import re
import json
from flask import request, jsonify
import urllib.request


def BenchmarkTest77006():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
