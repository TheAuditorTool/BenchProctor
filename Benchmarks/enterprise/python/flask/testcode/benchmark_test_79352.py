# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79352():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
