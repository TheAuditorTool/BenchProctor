# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59617():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
