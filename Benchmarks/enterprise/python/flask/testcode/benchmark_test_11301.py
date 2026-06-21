# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11301():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
