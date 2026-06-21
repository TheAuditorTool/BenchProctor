# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79650():
    referer_value = request.headers.get('Referer', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(referer_value))
    return jsonify({"result": "success"})
