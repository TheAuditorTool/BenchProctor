# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44964():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    eval(str(data))
    return jsonify({"result": "success"})
