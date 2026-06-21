# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74351():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
