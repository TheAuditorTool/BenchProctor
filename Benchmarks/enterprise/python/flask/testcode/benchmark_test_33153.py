# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest33153():
    multipart_value = request.form.get('multipart_field', '')
    data = ensure_str(multipart_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return jsonify({"result": "success"})
