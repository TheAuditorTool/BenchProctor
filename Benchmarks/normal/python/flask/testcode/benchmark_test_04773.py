# SPDX-License-Identifier: Apache-2.0
from flask import session
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest04773():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
