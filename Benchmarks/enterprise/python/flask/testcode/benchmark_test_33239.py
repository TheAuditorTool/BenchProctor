# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest33239():
    multipart_value = request.form.get('multipart_field', '')
    data = default_blank(multipart_value)
    if session.get('role') != 'admin':
        return jsonify({'error': 'forbidden'}), 403
    session['data'] = str(data)
    return jsonify({"result": "success"})
