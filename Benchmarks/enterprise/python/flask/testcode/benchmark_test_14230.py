# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14230():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
