# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06958():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
