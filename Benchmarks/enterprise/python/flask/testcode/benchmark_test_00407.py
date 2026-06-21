# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00407():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
