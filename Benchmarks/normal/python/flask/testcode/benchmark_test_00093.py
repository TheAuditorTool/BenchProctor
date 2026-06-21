# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00093():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
