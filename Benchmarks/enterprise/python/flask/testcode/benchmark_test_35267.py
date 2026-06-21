# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest35267():
    host_value = request.headers.get('Host', '')
    if not auth_check(session.get('user', ''), str(host_value)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
