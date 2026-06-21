# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30618():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
