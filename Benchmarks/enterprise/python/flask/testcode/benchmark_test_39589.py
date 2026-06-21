# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39589():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
