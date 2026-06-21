# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def BenchmarkTest69967():
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
