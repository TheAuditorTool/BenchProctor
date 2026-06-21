# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33982():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
