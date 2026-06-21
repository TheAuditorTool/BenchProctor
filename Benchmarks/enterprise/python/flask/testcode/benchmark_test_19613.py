# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest19613():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    session['data'] = str(data)
    return jsonify({"result": "success"})
