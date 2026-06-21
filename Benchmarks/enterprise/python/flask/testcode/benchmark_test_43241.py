# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43241():
    upload_name = request.files['upload'].filename
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(upload_name))
    return jsonify({"result": "success"})
