# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02738():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
