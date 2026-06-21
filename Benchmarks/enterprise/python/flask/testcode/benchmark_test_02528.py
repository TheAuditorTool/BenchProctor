# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import urllib.request


def to_text(value):
    return str(value).strip()

def BenchmarkTest02528():
    host_value = request.headers.get('Host', '')
    data = to_text(host_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
