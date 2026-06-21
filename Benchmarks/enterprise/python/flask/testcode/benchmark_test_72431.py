# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest72431():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    session['user'] = str(data)
    return jsonify({"result": "success"})
