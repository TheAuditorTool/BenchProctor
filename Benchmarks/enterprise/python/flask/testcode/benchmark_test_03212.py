# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03212():
    multipart_value = request.form.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
