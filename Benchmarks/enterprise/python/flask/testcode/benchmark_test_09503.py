# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest09503():
    origin_value = request.headers.get('Origin', '')
    data = default_blank(origin_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
