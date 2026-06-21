# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest64492():
    origin_value = request.headers.get('Origin', '')
    data = relay_value(origin_value)
    session['user'] = str(data)
    return jsonify({"result": "success"})
