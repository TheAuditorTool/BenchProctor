# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest18957():
    raw_body = request.get_data(as_text=True)
    data = ensure_str(raw_body)
    session['data'] = str(data)
    return jsonify({"result": "success"})
