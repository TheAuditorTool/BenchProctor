# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03132():
    origin_value = request.headers.get('Origin', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(origin_value))
    return jsonify({"result": "success"})
