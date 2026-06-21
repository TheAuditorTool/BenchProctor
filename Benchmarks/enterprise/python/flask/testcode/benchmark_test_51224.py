# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
from flask import request, jsonify


def BenchmarkTest51224():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
