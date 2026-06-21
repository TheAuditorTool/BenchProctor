# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33681():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
