# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest35855():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    session['data'] = str(data)
    return jsonify({"result": "success"})
