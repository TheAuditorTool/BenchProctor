# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest31805():
    origin_value = request.headers.get('Origin', '')
    data = str(origin_value).replace('\x00', '')
    session['data'] = str(data)
    return jsonify({"result": "success"})
