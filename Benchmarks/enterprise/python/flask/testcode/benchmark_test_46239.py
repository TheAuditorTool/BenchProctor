# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest46239():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    session['data'] = str(data)
    return jsonify({"result": "success"})
