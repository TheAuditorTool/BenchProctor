# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40319():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
