# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest33208():
    host_value = request.headers.get('Host', '')
    data = '{}'.format(host_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
