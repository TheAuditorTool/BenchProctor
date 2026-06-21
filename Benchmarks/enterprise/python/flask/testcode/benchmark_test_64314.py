# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64314():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
