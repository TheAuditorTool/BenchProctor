# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19207():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
