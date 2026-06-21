# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest03941():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    session['data'] = str(data)
    return jsonify({"result": "success"})
