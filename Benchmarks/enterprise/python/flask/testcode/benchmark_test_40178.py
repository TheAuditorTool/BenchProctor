# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40178():
    multipart_value = request.form.get('multipart_field', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(multipart_value) + ',data\n')
    return jsonify({"result": "success"})
