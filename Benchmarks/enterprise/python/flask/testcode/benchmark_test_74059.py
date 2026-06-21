# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest74059():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return jsonify({"result": "success"})
