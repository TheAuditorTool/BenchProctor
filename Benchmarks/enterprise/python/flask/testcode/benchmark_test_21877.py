# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21877():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
