# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest60091():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    session['data'] = str(data)
    return jsonify({"result": "success"})
