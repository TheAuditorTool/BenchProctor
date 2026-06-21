# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest81358():
    ua_value = request.headers.get('User-Agent', '')
    data = relay_value(ua_value)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
