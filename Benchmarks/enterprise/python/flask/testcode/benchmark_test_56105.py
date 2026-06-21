# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56105():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
