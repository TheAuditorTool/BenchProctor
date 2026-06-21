# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest64278():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    session['user'] = str(data)
    return jsonify({"result": "success"})
