# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41787():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
