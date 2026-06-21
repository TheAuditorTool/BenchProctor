# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12186():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
