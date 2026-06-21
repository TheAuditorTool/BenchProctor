# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04069():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
