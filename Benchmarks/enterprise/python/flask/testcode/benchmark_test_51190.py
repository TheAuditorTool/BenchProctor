# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest51190():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    session['user'] = str(data)
    return jsonify({"result": "success"})
