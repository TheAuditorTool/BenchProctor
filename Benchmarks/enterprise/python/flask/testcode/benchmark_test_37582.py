# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37582():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
