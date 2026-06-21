# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest24651():
    field_value = request.form.get('field', '')
    data = ensure_str(field_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
