# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35818():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
