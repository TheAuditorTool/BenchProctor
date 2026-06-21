# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45384():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
