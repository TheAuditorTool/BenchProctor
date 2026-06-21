# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest14853():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
