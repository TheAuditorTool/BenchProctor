# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59905():
    field_value = request.form.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return jsonify({"result": "success"})
