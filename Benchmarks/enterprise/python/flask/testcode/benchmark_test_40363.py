# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest40363():
    field_value = request.form.get('field', '')
    data = coalesce_blank(field_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session['data'] = str(data)
    return jsonify({"result": "success"})
