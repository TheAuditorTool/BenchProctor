# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51808():
    upload_name = request.files['upload'].filename
    data, _sep, _rest = str(upload_name).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
