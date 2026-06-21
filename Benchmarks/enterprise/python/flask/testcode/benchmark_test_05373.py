# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05373():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
