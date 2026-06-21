# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest53972():
    referer_value = request.headers.get('Referer', '')
    if not auth_check(session.get('user', ''), str(referer_value)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
