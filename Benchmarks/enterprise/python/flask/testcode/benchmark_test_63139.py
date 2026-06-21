# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest63139():
    origin_value = request.headers.get('Origin', '')
    data = coalesce_blank(origin_value)
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
