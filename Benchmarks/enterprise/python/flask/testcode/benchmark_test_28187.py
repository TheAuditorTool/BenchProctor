# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28187():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
