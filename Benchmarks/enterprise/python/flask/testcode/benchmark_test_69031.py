# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest69031():
    auth_header = request.headers.get('Authorization', '')
    session['data'] = str(auth_header)
    return jsonify({"result": "success"})
