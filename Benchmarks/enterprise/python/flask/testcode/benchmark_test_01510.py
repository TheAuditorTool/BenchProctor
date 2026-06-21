# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01510():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    int(str(data))
    return jsonify({"result": "success"})
