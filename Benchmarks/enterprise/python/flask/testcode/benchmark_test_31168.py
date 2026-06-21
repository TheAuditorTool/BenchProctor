# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31168():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
