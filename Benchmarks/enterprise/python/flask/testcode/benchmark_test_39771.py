# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39771():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
