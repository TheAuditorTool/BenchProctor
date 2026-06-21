# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66887():
    upload_name = request.files['upload'].filename
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
