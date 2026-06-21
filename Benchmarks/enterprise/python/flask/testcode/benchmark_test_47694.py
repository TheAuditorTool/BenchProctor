# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47694():
    multipart_value = request.form.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
