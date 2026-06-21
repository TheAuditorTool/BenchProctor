# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest00188():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return jsonify({"result": "success"})
