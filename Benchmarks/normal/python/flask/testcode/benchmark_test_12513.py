# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12513():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return jsonify({"result": "success"})
