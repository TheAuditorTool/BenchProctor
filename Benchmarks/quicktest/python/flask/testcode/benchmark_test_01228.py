# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest01228():
    multipart_value = request.form.get('multipart_field', '')
    data = relay_value(multipart_value)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
