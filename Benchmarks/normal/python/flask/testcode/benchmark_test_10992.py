# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10992():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
