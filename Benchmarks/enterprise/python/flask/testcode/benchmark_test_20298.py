# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20298():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
