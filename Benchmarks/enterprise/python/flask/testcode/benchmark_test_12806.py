# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12806():
    multipart_value = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
