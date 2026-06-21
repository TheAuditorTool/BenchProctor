# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest47817():
    raw_body = request.get_data(as_text=True)
    session['data'] = str(raw_body)
    return jsonify({"result": "success"})
