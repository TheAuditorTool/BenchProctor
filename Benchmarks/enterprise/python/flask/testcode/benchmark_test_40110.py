# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40110():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
