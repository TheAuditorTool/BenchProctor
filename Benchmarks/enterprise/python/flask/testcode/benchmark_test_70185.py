# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest70185():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    session['data'] = str(data)
    return jsonify({"result": "success"})
