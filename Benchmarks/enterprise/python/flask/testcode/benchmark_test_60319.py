# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60319():
    multipart_value = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
