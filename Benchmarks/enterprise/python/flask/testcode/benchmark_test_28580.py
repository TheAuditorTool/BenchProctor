# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28580():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
