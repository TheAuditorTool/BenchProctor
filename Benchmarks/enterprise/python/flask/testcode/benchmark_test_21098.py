# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21098():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
