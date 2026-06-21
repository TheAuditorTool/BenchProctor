# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest73391():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
