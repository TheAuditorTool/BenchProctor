# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05080():
    ua_value = request.headers.get('User-Agent', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(ua_value))
    return jsonify({"result": "success"})
