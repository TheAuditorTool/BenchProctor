# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest42954():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    session['user'] = str(data)
    return jsonify({"result": "success"})
