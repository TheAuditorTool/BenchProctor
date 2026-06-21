# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest41517():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    if session.get('role') != 'admin':
        return jsonify({'error': 'forbidden'}), 403
    session['data'] = str(data)
    return jsonify({"result": "success"})
