# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07420():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
