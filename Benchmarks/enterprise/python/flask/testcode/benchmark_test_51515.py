# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest51515():
    referer_value = request.headers.get('Referer', '')
    data = default_blank(referer_value)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
