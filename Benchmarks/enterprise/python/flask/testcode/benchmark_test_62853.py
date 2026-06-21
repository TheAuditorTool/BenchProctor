# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62853():
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
