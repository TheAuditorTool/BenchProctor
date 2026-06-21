# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest48097():
    referer_value = request.headers.get('Referer', '')
    data = coalesce_blank(referer_value)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
