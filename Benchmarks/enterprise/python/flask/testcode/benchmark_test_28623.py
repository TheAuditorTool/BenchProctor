# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28623():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
