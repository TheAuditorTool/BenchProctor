# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest66814():
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return jsonify({"result": "success"})
