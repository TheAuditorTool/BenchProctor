# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61024():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    exec(str(data))
    return jsonify({"result": "success"})
