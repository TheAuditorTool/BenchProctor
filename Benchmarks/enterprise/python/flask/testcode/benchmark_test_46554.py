# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest46554():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if json_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = json_value
    session['data'] = str(processed)
    return jsonify({"result": "success"})
