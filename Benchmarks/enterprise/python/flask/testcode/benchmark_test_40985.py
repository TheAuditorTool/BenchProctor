# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40985():
    multipart_value = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
