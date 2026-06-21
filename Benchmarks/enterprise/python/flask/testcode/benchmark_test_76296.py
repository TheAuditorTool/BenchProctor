# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest76296():
    header_value = request.headers.get('X-Custom-Header', '')
    data = normalise_input(header_value)
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requests.get(str(processed))
    return jsonify({"result": "success"})
