# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest17701():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    session['user'] = str(data)
    return jsonify({"result": "success"})
