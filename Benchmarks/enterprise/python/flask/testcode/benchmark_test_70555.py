# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70555():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
