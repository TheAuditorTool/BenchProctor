# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66491():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
