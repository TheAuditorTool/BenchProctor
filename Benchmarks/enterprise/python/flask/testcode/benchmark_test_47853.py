# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47853():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
