# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest23230():
    auth_header = request.headers.get('Authorization', '')
    data = '{}'.format(auth_header)
    session['data'] = str(data)
    return jsonify({"result": "success"})
