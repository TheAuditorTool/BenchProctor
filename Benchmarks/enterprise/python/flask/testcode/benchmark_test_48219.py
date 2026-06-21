# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48219():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
