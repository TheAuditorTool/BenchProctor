# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37219():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
