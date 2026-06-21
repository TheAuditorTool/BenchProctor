# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest04254():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    session['user'] = str(data)
    return jsonify({"result": "success"})
