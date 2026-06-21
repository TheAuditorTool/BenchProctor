# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10627():
    upload_name = request.files['doc'].filename
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
