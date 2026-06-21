# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
from flask import request, jsonify


def BenchmarkTest79470():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
