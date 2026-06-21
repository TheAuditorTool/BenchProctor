# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest52932():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
