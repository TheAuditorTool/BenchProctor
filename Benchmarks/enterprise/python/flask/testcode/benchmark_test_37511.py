# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37511():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % (forwarded_ip,)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
