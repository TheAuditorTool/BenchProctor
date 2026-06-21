# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest55252():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    session['data'] = str(data)
    return jsonify({"result": "success"})
