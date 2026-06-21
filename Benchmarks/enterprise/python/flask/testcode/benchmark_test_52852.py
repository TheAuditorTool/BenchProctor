# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52852():
    multipart_value = request.form.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    int(str(data))
    return jsonify({"result": "success"})
