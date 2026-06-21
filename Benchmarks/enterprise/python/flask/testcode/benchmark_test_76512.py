# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest76512():
    ua_value = request.headers.get('User-Agent', '')
    data = normalise_input(ua_value)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    exec(str(processed))
    return jsonify({"result": "success"})
