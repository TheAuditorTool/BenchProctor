# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00886():
    upload_name = request.files['upload'].filename
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return jsonify({"result": "success"})
