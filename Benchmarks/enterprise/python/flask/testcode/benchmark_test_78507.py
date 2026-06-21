# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest78507():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    session['data'] = str(data)
    return jsonify({"result": "success"})
