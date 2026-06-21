# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06252():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
