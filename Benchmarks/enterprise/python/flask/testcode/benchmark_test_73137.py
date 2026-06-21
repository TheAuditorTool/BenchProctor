# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest73137():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    session['data'] = str(data)
    return jsonify({"result": "success"})
