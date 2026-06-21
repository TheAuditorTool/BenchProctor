# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest75959():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
