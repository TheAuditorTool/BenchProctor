# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30152():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
