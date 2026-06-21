# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11723():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    int(str(data))
    return jsonify({"result": "success"})
