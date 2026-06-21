# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70331():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    int(str(data))
    return jsonify({"result": "success"})
