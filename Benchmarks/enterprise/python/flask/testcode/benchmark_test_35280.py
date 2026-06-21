# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest35280():
    host_value = request.headers.get('Host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
