# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest74048():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    session['user'] = str(data)
    return jsonify({"result": "success"})
