# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest32430():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    session['data'] = str(data)
    return jsonify({"result": "success"})
