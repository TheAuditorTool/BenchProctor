# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53029():
    upload_name = request.files['upload'].filename
    try:
        result = int(str(upload_name))
    except Exception:
        pass
    return jsonify({"result": "success"})
