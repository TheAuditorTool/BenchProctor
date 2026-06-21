# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest72309():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    session['data'] = str(data)
    return jsonify({"result": "success"})
