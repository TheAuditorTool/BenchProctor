# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25389():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
