# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest70786():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    session['data'] = str(data)
    return jsonify({"result": "success"})
