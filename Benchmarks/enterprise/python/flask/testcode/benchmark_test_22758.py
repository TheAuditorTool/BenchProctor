# SPDX-License-Identifier: Apache-2.0
from flask import session
import json
from flask import request, jsonify


def BenchmarkTest22758():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
