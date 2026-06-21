# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24627():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
