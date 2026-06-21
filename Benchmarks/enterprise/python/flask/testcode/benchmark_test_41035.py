# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest41035():
    multipart_value = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
