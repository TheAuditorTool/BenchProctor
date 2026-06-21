# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25151():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
