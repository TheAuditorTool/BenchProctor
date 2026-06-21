# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18440():
    multipart_value = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
