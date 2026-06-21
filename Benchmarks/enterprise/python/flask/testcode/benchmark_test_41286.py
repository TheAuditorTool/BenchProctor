# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest41286():
    multipart_value = request.form.get('multipart_field', '')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session['data'] = str(multipart_value)
    return jsonify({"result": "success"})
