# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest43616():
    referer_value = request.headers.get('Referer', '')
    data = to_text(referer_value)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
