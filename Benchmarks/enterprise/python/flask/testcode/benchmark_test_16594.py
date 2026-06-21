# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16594():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
