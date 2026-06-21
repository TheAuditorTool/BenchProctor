# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40959():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
