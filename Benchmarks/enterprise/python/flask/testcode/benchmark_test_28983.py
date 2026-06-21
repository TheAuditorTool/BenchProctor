# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28983():
    upload_name = request.files['upload'].filename
    data = f'{upload_name}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
