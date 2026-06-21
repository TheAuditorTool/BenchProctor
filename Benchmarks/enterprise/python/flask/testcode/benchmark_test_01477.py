# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest01477():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
