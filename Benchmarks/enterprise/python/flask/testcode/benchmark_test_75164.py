# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75164():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
