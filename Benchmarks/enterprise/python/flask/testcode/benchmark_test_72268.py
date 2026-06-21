# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72268():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    int(str(data))
    return jsonify({"result": "success"})
