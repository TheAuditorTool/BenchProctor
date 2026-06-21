# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest16016():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    os.remove(str(data))
    return jsonify({"result": "success"})
