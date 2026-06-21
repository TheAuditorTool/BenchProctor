# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11945():
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
