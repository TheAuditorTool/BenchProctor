# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79834():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
