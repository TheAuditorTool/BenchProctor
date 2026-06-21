# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65072():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(forwarded_ip))
    return jsonify({"result": "success"})
