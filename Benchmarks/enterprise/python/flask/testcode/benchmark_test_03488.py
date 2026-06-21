# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest03488():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return jsonify({"result": "success"})
