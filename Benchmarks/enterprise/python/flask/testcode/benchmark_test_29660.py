# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29660():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
