# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75089():
    multipart_value = request.form.get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return jsonify({"result": "success"})
