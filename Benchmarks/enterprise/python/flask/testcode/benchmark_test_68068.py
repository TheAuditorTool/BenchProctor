# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68068():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
