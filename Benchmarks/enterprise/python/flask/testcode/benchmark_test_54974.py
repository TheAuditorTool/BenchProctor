# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54974():
    field_value = request.form.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return jsonify({"result": "success"})
