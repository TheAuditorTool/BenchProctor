# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08003():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
