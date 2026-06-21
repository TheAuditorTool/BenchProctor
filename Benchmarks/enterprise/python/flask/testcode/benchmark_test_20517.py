# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20517():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    eval(str(data))
    return jsonify({"result": "success"})
